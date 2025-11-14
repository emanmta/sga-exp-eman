from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from app.schemas.auth import LoginIn
from app.server.dependencies import get_settings
from app.db.connection import get_db_connection

router = APIRouter()
bearer = HTTPBearer(auto_error=True)
settings = get_settings()


# Dependency to get DB connection and cursor
def get_db():
    conn = get_db_connection()
    try:
        yield conn.cursor()
    finally:
        conn.close()


@router.post("/login", operation_id="login")
def login(body: LoginIn, cursor=Depends(get_db)):
    # 1. Cari pengguna berdasarkan username
    # Pastikan Anda mengambil password juga dari DB
    cursor.execute(
        "SELECT id, password, role, department FROM users WHERE username = %s;",
        (body.username,),
    )
    user = cursor.fetchone()

    # 2. Periksa apakah pengguna ada DAN passwordnya cocok
    if not user or user["password"] != body.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # 3. Jika berhasil, buat token
    token = jwt.encode(
        {
            "sub": str(user["id"]),
            "role": user["role"],
            "department": user["department"],
        },
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    return {"access_token": token, "token_type": "bearer"}


def get_user_id_from_header(
    creds: HTTPAuthorizationCredentials = Depends(bearer),
) -> str:
    token = creds.credentials
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
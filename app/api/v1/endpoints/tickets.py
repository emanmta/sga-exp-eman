from fastapi import APIRouter, status, Depends
from app.schemas.ticket import Ticket, TicketCreate
from app.api.v1.routers.auth import RoleChecker

router = APIRouter()

allowed_roles = ["guest", "customer service"]

@router.post(
    "/",
    response_model=Ticket,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new ticket",
    description="Receives ticket data, validates it, and returns the created ticket with generated fields.",
    dependencies=[Depends(RoleChecker(allowed_roles))]
)
def create_ticket(ticket_in: TicketCreate):
    """
    ## Create a new ticket
    
    This endpoint simulates the creation of a new guest ticket.
    
    - **Receives:** A JSON object with `guest_name`, `room_number`, `category`, and `description`.
    - **Returns:** A full ticket object including a generated `id`, `status`, `priority`, and `created_at`.
    
    *(Note: Currently, this does not save to a database.)*
    """
    # For now, we just convert the input schema to the full ticket schema
    # In the future, this is where we would save the ticket to the database
    ticket_data = ticket_in.dict()
    new_ticket = Ticket(**ticket_data)
    
    return new_ticket
from pydantic import BaseModel, Field
import uuid
from datetime import datetime
from enum import Enum

class TicketStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class TicketPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TicketBase(BaseModel):
    guest_name: str = Field(..., example="John Doe")
    room_number: str = Field(..., example="101")
    category: str = Field(..., example="Maintenance")
    description: str = Field(..., example="The air conditioner is not working.")

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    status: TicketStatus = TicketStatus.OPEN
    priority: TicketPriority = TicketPriority.MEDIUM
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
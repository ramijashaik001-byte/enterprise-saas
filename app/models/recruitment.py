from sqlalchemy import Column, String, Integer, Text
from app.models.base import TenantBase

class JobOpening(TenantBase):
    """
    Job postings/positions listed by the company.
    """
    __tablename__ = "job_openings"
    
    title = Column(String, nullable=False)
    department = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    requirements = Column(Text, nullable=True)
    status = Column(String, default="draft") # draft, open, closed

class Applicant(TenantBase):
    """
    Candidates applying for a JobOpening.
    """
    __tablename__ = "applicants"
    
    job_opening_id = Column(Integer, nullable=False, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    resume_url = Column(String, nullable=True)
    status = Column(String, default="applied") # applied, reviewing, interviewing, offered, rejected, hired

# Extension hooks for Applicant records tracker

# PR trigger comment for recruitment

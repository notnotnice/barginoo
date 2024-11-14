from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set

from uuid import uuid4


class User:
    def __init__(
            self, ref: uuid4, username: str, email: str, password: str
        ) -> None:
        self.ref = ref
        self.username = username
        self.email = email
        self.password = password


class UserProfile:
    def __init__(
            self, user: User, avatar: Optional[str], gender: Optional[str],
            birth_date: Optional[date], location: Optional[str],
            bio: Optional[str] 
        ) -> None:
        self.user = user
        self.avatar = avatar
        self.gender = gender
        self.birth_date = birth_date
        self.location = location
        self.bio = bio
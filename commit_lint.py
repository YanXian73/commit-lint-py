from dataclasses import dataclass
import re

CONVENTIONAL_COMMIT_PATTERN = re.compile(
      r"^(feat|fix|docs|refactor|test|chore)(\([^)]+\))?: .+"
  )
@dataclass(frozen=True)
class Ok:
    pass


@dataclass(frozen=True)
class Failed:
    reason: str


type LintResult = Ok | Failed


class CommitLinter:
    def lint(self, message: str) -> LintResult:
        # raise NotImplementedError("not implemented yet")
        if not CONVENTIONAL_COMMIT_PATTERN.match(message):
            return Failed(reason="Invalid commit message format.")
        if len(message) > 50:
            return Failed(reason=f"Subject too long: {len(message)} characters (max 50)")
        if message.endswith("."):
            return Failed(reason="Subject should not end with a period.")
        return Ok()
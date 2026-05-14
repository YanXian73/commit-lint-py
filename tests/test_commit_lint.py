from commit_lint import CommitLinter, Failed, Ok


def test_short_message_passes():
    linter = CommitLinter()
    result = linter.lint("feat: add login")
    assert result == Ok()


def test_subject_longer_than_50_chars_fails():
    linter = CommitLinter()
    long_subject = "feat: " + "a" * 51
    result = linter.lint(long_subject)

    match result:
        case Failed(reason=reason):
            assert "too long" in reason.lower()
        case _:
            assert False, f"Expected Failed, got {result}"


def test_subject_ending_with_period_fails():
    linter = CommitLinter()
    result = linter.lint("hello.")

    match result:
        case Failed(reason=reason):
            assert "period" in reason.lower() or "." in reason
        case _:
            assert False, f"Expected Failed, got {result}"


def test_message_without_valid_type_fails():
    linter = CommitLinter()
    result = linter.lint("updated readme")

    match result:
        case Failed(reason=reason):
            assert "type" in reason.lower() or "format" in reason.lower()
        case _:
            assert False, f"Expected Failed, got {result}"

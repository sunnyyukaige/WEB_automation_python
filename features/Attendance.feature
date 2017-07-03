Feature: Mark attendance include (mark, overwrite and view)function

Scenario Outline: Teacher can go to Attendance page with students info
    Given I am a teacher
    When I go to mark attendance <view>
    Then I can check the students attendance <status> in <view>
    Examples: View
        |view|status|
        |Session|Unknown|
        |Course|Unknown |

Scenario Outline: Teacher mark attendance for students
    Given I am a teacher
    When I can mark <status> attendance in <view>
    Then  I can check the students attendance <status> in <view>
    Examples: View
        |view|status|
        |Session|PRESENT|
        |Session|ABSENT |
        |Session|LATE|
        |Course|PRESENT|
        |Course|ABSENT |
        |Course|LATE|
        |Course|NA|

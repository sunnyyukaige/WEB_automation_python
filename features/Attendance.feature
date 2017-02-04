Feature:Mark attendance include (mark, overwrite and view)function

    Scenario Outline: Teacher can go to Attendance page with students info
     Given I am a teacher
     When I go to mark attendance <view>
     Then I can check the students attendance info

   Examples: View
             |view|
             |Day|
             |Course|
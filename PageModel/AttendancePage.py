__author__ = 'sunny.yu2 & sophia.lee'
from PageModel.BasePage import BasePage
from WebElement.By import By
from WebElement.Waitor import Waitor
import time

class AttendancePage(BasePage):

    def markAttendanceViewClick(self):
        switchBtn =self.browser.find_web_element(By.CLASS_NAME, 'test-view-switch-session')
        switchBtn.click()

    def doMarkAttendance(self, status, view):
        MarkBtn = self.browser.find_web_element(By.CLASS_NAME, 'test-viewnav-button-mark')
        MarkBtn.wait_for().visible()
        MarkBtn.click()
        if (view == 'Session'):
            PublishBtn = self.browser.find_web_element(By.CLASS_NAME, 'test-toolbar-button-publish')
            PublishBtn.wait_for().visible()
            if (status == 'PRESENT'):
                GetPresentBtn = self.browser.find_web_elements(By.CLASS_NAME, 'test-mark-present-btn')
                PresentBtn = GetPresentBtn[0]
                PresentBtn.click()
            elif (status == 'ABSENT'):
                GetAbsentBtn = self.browser.find_web_elements(By.CLASS_NAME, 'test-mark-absent-btn')
                AbsentBtn = GetAbsentBtn[0]
                AbsentBtn.click()
            elif (status == 'LATE'):
                GetLateBtn = self.browser.find_web_elements(By.CLASS_NAME, 'test-mark-late-btn')
                LateBtn = GetLateBtn[0]
                LateBtn.click()
            else:
                pass
            PublishBtn.click()
            time.sleep(1)
        elif(view == 'Course'):
            ExitBtn = self.browser.find_web_element(By.CLASS_NAME, 'test-toolbar-button-exit')
            ExitBtn.wait_for().visible()
            GetStudentAttendanceBtn = self.browser.find_web_elements(By.CLASS_NAME, 'test-highlighted')
            FirstStudentAttendanceBtn=GetStudentAttendanceBtn[2]
            FirstStudentAttendanceBtn.click()
            if (status == 'PRESENT'):
                GetPresentBtn = FirstStudentAttendanceBtn.find_web_element(By.CLASS_NAME, 'test-dropdown-present')
                GetPresentBtn.click()
            elif (status == 'ABSENT'):
                GetAbsentBtn = FirstStudentAttendanceBtn.find_web_element(By.CLASS_NAME, 'test-dropdown-absent')
                GetAbsentBtn.click()
            elif (status == 'LATE'):
                GetLateBtn = FirstStudentAttendanceBtn.find_web_element(By.CLASS_NAME, 'test-dropdown-late')
                GetLateBtn.click()
            elif(status == 'NA'):
                GetNABtn = FirstStudentAttendanceBtn.find_web_element(By.CLASS_NAME, 'test-dropdown-not-applicable')
                GetNABtn.click()
            else:
                pass
            ExitBtn.click()
            time.sleep(1)
        else:
            pass

    def checkStudentAttendanceInfo(self, status, view):
        isTure = False
        MarkBtn = self.browser.find_web_element(By.CLASS_NAME, 'test-viewnav-button-mark')
        MarkBtn.wait_for().visible()
        if (view == 'Session'):
            getAttenadanceInfo = self.browser.find_web_elements(By.CLASS_NAME, 'test-student-attendance-status')
            attendanceInfo = getAttenadanceInfo[0].getText
            print(attendanceInfo)
            if (status == 'Unknown'):
                if attendanceInfo in [u'UNMARKED', u'LATE', u'ABSENT', u'PRESENT']:
                    isTure = True
                else:
                    pass
            elif (status == attendanceInfo):
                isTure = True
            else:
                pass
        else:
            GetStudentsAttendanceStatus = self.browser.find_web_elements(By.CLASS_NAME, 'test-highlighted')
            FirstStudentAttendance = GetStudentsAttendanceStatus[2]
            if (status == 'PRESENT'):
                FirstStudentAttendanceStatus = FirstStudentAttendance.find_web_element(By.CLASS_NAME, 'test-present')
                if FirstStudentAttendanceStatus.exist():
                    isTure = True
            elif (status == 'ABSENT'):
                FirstStudentAttendanceStatus = FirstStudentAttendance.find_web_element(By.CLASS_NAME, 'test-absent')
                if FirstStudentAttendanceStatus.exist():
                    isTure = True
            elif (status == 'LATE'):
                FirstStudentAttendanceStatus = FirstStudentAttendance.find_web_element(By.CLASS_NAME, 'test-late')
                if FirstStudentAttendanceStatus.exist():
                    isTure = True
            elif (status == 'NA'):
                FirstStudentAttendanceStatus = FirstStudentAttendance.find_web_element(By.CLASS_NAME, 'test-attendance-cell')
                Status = FirstStudentAttendanceStatus.getText
                if (Status == 'n/a'):
                    isTure = True
            else:
                if GetStudentsAttendanceStatus.__len__() >0:
                    isTure = True
        return isTure





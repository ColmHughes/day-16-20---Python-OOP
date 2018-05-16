class Report():
    
    
    def __init__(self):
        self.content = 0
    
    
    def _print_header(self):
        print("This is the header")
        
    def _print_body(self):
        print("This is the body")
    
    def _print_footer(self):
        print("This is the footer")
    
    def print_report(self):
        self._print_header()
        self._print_body()
        self._print_footer()
        
        
        
class UpperCaseReport(Report):
    def _print_body(self):
        print("UPPER CASE REPORT")
        
        
        
report = UpperCaseReport()
report.print_report()
    
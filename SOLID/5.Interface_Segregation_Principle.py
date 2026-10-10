#Clients should not be forced to depend on (implement) methods they do not use.
# It is better to have several small,
# specialized interfaces than one large,
# general-purpose interface.

from abc import ABC, abstractmethod
# Each interface represents only ONE capability (segregated interfaces)
class Printable(ABC):
    @abstractmethod
    def print_document(self, doc):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self, doc):
        pass

class Faxable(ABC):
    @abstractmethod
    def fax_document(self, doc):
        pass

class Staplable(ABC):
    @abstractmethod
    def staple_document(self, doc):
        pass


# All-in-one office printer inherits from every interface it actually needs
class OfficeAllInOnePrinter(Printable, Scannable, Faxable, Staplable):
    def print_document(self, doc):
        print(f"Printing {doc}...")

    def scan_document(self, doc):
        print(f"Scanning {doc}...")

    def fax_document(self, doc):
        print(f"Faxing {doc}...")

    def staple_document(self, doc):
        print(f"Stapling {doc}...")


# Simple home printer only inherits Printable - no useless/broken methods
class SimpleHomePrinter(Printable):
    def print_document(self, doc):
        print(f"Printing {doc}...")


# Printer+Scanner combo only implements what it actually supports
class PrinterScanner(Printable, Scannable):
    def print_document(self, doc):
        print(f"Printing {doc}...")

    def scan_document(self, doc):
        print(f"Scanning {doc}...")


# This function only depends on the Printable interface,
# not on the whole MultiFunctionPrinter - that's the ISP benefit
def print_job(device: Printable, doc):
    device.print_document(doc)


# --- Usage ---
home_printer = SimpleHomePrinter()
print_job(home_printer, "report.pdf")  # Works fine, no risk of crashing

office_printer = OfficeAllInOnePrinter()
print_job(office_printer, "contract.pdf")
office_printer.fax_document("contract.pdf")
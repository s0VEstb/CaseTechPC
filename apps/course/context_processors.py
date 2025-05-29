from .models.contacts import Contacts

def contact_info(request):
    """
    Context processor to add contact information to all templates
    """
    contacts = Contacts.objects.first()
    return {
        'footer_contacts': contacts
    } 
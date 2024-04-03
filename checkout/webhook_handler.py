from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        # assign request as an attribute of this class called request(access to request data)
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
"""Buttons."""
from flow.engine import Extension

class Buttons(Extension):
    """
    Buttons plugin.

    This pseudo function will be called on each BBot->setResponse() and will
    provide buttons to the output if isButton attr is true will not be needed
    with flow2
    """


    def __init__(self, flow):
        super().__init__(flow)
        class_name = self.__class__.__module__ + '.' + self.__class__.__name__
        flow.register_dot_flow_function('buttons', {
            'class': class_name, 'method': 'get_response'})


    def get_response(self, node):
        """Get response for node."""
        output = self.get_buttons(node)
        for out in output:
            self.flow.set_output('buttons', out)


    def get_buttons(self, node):
        buttons = []
        for conn in node['connections']:
            if 'isButton' in conn and conn['is_button']:
                label = conn['if']['value'][0]
                if 'name' in conn and len(conn['name']) > 0:
                    label = conn['name']
                buttons.append(
                    {
                        'label': label,
                        'input': conn['if']['value'][0]
                    }
                )
        return buttons
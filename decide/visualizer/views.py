import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            optionsG = r[0].get('question').get('options')
            optionsName = []

            for dicc in optionsG:
                optionsName.append(dicc.get('option'))

            votesG = r[0].get('postproc')
            numbVotes = []

            for dicc in votesG:
                numbVotes.append(dicc.get('postproc'))
            print(context)

            context['voting'] = json.dumps(r[0])
            context['optVotes'] = optionsName
            context['numVotes'] = numbVotes
            print(context)
        except:
            raise Http404

        return context

    # def get_votes_graphic(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     vid = kwargs.get('voting_id', 0)

    #     try:
    #         r = mods.get('voting', params={'id': vid})
    #         optionsG = r[0].get('question').get('options')
    #         optionsName = []

    #         for dicc in optionsG:
    #             optionsName.append(dicc.get('option'))

    #         votesG = r[0].get('postproc')
    #         numbVotes = []

    #         for dicc in votesG:
    #             numbVotes.append(dicc.get('postproc'))
    #         print(optionsName)
    #         print(json.dumps(optionsName))

    #         context['optVotes'] = json.dumps(optionsName)
    #         context['numVotes'] = numbvotes
    #     except:
    #         raise Http404

    #     return context

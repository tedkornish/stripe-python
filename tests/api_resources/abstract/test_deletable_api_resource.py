from __future__ import absolute_import, division, print_function

import stripe


class TestDeletableAPIResource(object):
    class MyDeletable(stripe.api_resources.abstract.DeletableAPIResource):
        pass

    def test_delete(self, request_mock):
        request_mock.stub_request(
            'delete',
            '/v1/mydeletables/mid',
            {
                'id': 'mid',
                'deleted': True,
            }
        )

        obj = self.MyDeletable.construct_from({
            'id': 'mid'
        }, 'mykey')

        assert obj is obj.delete()
        request_mock.assert_requested(
            'delete',
            '/v1/mydeletables/mid',
            {}
        )
        assert obj.deleted is True
        assert obj.id == 'mid'

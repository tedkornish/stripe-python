from __future__ import absolute_import, division, print_function

import stripe


class TestCreateableAPIResource(object):
    class MyCreatable(stripe.api_resources.abstract.CreateableAPIResource):
        pass

    def test_create(self, request_mock):
        request_mock.stub_request(
            'post',
            '/v1/mycreatables',
            {
                'object': 'charge',
                'foo': 'bar',
            }
        )

        res = self.MyCreatable.create()

        request_mock.assert_requested(
            'post',
            '/v1/mycreatables',
            {}
        )
        assert isinstance(res, stripe.Charge)
        assert res.foo == 'bar'

    def test_idempotent_create(self, request_mock):
        request_mock.stub_request(
            'post',
            '/v1/mycreatables',
            {
                'object': 'charge',
                'foo': 'bar',
            }
        )

        res = self.MyCreatable.create(idempotency_key='foo')

        request_mock.assert_requested(
            'post',
            '/v1/mycreatables',
            {},
            {'Idempotency-Key': 'foo'}
        )
        assert isinstance(res, stripe.Charge)
        assert res.foo == 'bar'

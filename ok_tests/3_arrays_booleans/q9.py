test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [

      {
          'code': r"""
          >>> # It looks like you have accidentally changed some of the elements in the `psychosis_status_observations_array`. Please run the following code to restore it to its proper state: psychosis_status_observations_array = np.array(['psychotic', 'not_psychotic', 'not_psychotic', 'not_psychotic', 'psychotic'])
          >>> np.array_equiv(psychosis_status_observations_array, np.array(['psychotic', 'not_psychotic', 'not_psychotic', 'not_psychotic', 'psychotic'])) == True
          True

          """,
          'hidden': False,
          'locked': False
        },

        {
          'code': r"""
          >>> # Hmmm, psychotic_obs does not contain the correct values. Did you use the `is_psychotic_boolean_array` as a Boolean index on the `psychosis_status_observations_array`?
          >>> np.array_equiv(psychotic_obs, np.array(['psychotic', 'psychotic'])) == True
          True

          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

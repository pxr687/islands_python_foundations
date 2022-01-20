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
          >>> # Hmmm, is_psychotic_boolean_array does not contain the correct values. It should be a Boolean array containing a True where the corresponding element of the psychosis_status_observations_array` is 'psychotic'.
          >>> np.array_equiv(is_psychotic_boolean_array, np.array([ True, False, False, False,  True])) == True
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

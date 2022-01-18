test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [

      {
          'code': r"""
          >>> # It looks like you have accidentally changed some of the elements in the `psychosis_scores_array`. Please run the following code to restore it to its proper state: psychosis_scores_array = np.array([80, 20, 14, 13, 91])
          >>> np.array_equiv(psychosis_scores_array, np.array([80, 20, 14, 13, 91])) == True
          True

          """,
          'hidden': False,
          'locked': False
        },

        {
          'code': r"""
          >>> # Hmmm, very_low_scores_boolean_array does not contain the correct values. It should be a Boolean array containing a True where the corresponding element of the psychosis_scores_array is *less than or equal to* 14.
          >>> np.array_equiv(very_low_scores_boolean_array, np.array([False, False,  True,  True, False])) == True
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

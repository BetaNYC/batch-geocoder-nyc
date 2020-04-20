function getStatus({ features, selectedFeatureId, approved, pending }) {
  let status = (!pending && (features.length === 0 || approved === false))
    ? 'Failed'
    : pending
      ? 'Pending'
      : approved === true
        ? 'Approved'
        : 'Doubt'

  return {
    status,
    color: colorLookup(status)
  }
}

function colorLookup(status) {
  switch (status) {
    case 'Pending':
      return '#9e9e9e'
    case 'Approved':
      return '#8bc34a'
    case 'Doubt':
      return '#ff9800'
    case 'Failed':
      return '#f44336'
    default:
      return '#fff'
  }
}

export default getStatus
function getStatus({ features, checked, pending }) {
  let status = (!pending && (features.length === 0 || checked === false))
    ? 'Failed'
    : pending
      ? 'Pending'
      : checked === true
        ? 'Checked'
        : 'Unchecked'

  return {
    status,
    color: colorLookup(status)
  }
}

function colorLookup(status) {
  switch (status) {
    case 'Pending':
      return '#9e9e9e'
    case 'Checked':
      return '#8bc34a'
    case 'Unchecked':
      return '#ff9800'
    case 'Failed':
      return '#f44336'
    default:
      return '#fff'
  }
}

export default getStatus
// Require all test components
const testsContext = require.context('./js', true, /^.+\.spec\.jsx?$/);
testsContext.keys().forEach(testsContext);

// Require all components
const componentsContext = require.context('./js', true, /^.+\.jsx?$/);
componentsContext.keys().forEach(componentsContext);

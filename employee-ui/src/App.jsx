import { gql, useQuery } from "@apollo/client";
const GET_EMPLOYEES = gql`
  query {
    allEmployees {
      edges {
        node {
          id
          name
          email
          department
          salary
        }
      }
    }
  }
`;

function App() {
  const { loading, error, data } = useQuery(GET_EMPLOYEES);
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;
  return (
    <div>
      <h2>Employees</h2>
      {data.allEmployees.edges.map(({ node }) => (
        <div key={node.id}>
          <h4>{node.name}</h4>
          <p>{node.department} - ₹{node.salary}</p>
        </div>
      ))}
    </div>
  );
}
export default App;


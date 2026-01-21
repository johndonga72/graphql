import { gql } from "@apollo/client";

export const GET_EMPLOYEES = gql`
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

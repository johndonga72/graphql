import { ApolloClient, InMemoryCache } from "@apollo/client";
const client = new ApolloClient({
    uri: "https://graphql-lzcc.onrender.com",
    cache: new InMemoryCache(),
});
export default client;
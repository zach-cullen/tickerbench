import styles from "./page.module.css";
import { useRouter } from 'next/router';

export default const Echo = ({message}) => {

  const router = useRouter();
  const { message } = router.query;


  return (
    <main className={styles.main}>
      <h1>{message}</h1>
    </main>
  );
}
import styles from './layout.module.scss';
import Head from "next/head";
import utilStyles from '../styles/utils.module.scss';
import Image from 'next/image';
import Link from 'next/link';

const name = "Gohdong"
export const siteTitle = 'Next.js Sample Website'

export default function Layout({children, home}: { children: any, home: any }) {
    console.log(children)
    return (
        <div className={styles.container}>
            <Head>
                <link rel="icon" href="/favicon.ico"/>
                <meta
                    name="description"
                    content={"Learn how to build a personal website using NEXT JS"}
                />
                <meta
                    property="og:image"
                    content={`https://og-images.vercel.app/${encodeURI(siteTitle)}.png`}
                />
            </Head>
            <header className={styles.header}>
                {
                    home ? (
                        <>
                            <Image
                                priority
                                src="/images/a.png"
                                className={utilStyles.borderCircle}
                                height={144}
                                width={144}
                                alt={name}
                            />
                            <h1 className={utilStyles.heading2Xl}>{name}</h1>
                        </>
                    ) : (
                        <><Link href="/">
                            <a>
                                <Image
                                    priority
                                    src="/images/a.png"
                                    className={utilStyles.borderCircle}
                                    height={108}
                                    width={108}
                                    alt={name}
                                />
                            </a>
                        </Link>
                            <h2 className={utilStyles.headingLg}>
                                <Link href="/">
                                    <a className={utilStyles.colorInherit}>{name}</a>
                                </Link>
                            </h2>
                        </>
                    )
                }
            </header>
            <main>{children}</main>
            {!home && (
                <div className={styles.backToHome}>
                    <Link href="/">
                        <a>Back to home</a>
                    </Link>
                </div>
            )}

        </div>)
}
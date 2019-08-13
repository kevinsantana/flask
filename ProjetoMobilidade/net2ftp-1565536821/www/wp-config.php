<?php
/** Enable W3 Total Cache */
define('WP_CACHE', true); // Added by W3 Total Cache

/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'projetomobilid' );

/** MySQL database username */
define( 'DB_USER', 'projetomobilid' );

/** MySQL database password */
define( 'DB_PASSWORD', 'Mob102030' );

/** MySQL hostname */
define( 'DB_HOST', 'mysql.projetomobilidade.com' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',          'L9EfH4-1+v5X,iA])yB[rz+8P7-.,y2ts<:>[PX^Ou?IX%>DJHE$)*l!g7xIZn>T' );
define( 'SECURE_AUTH_KEY',   ',3Ei,i|dhgn5[X9{KXy6Rbd2_D_!rIs!~Z2-=}5/G7`.OQrPqH75oFTx=eXTvXEo' );
define( 'LOGGED_IN_KEY',     '_nC^<}Z)>|^[Kg%vI;X+3I~0^;st? f,$ayr8-]a)MN;^c5!ssCgGS4e(s`<`YFA' );
define( 'NONCE_KEY',         '9dDmx=*Yy6&A;q]_pH8Ckusxnt3T[{.`,fYb*XNg2C@MDO+vP|QCk8GPJc0m`% T' );
define( 'AUTH_SALT',         'o}4?S<&P~9`T.vl`%-fz#^TO5g};6MFDx2ht;qgdg4mJd#+Pm4Ttpl,N_l^7!~3G' );
define( 'SECURE_AUTH_SALT',  'f--~![u.3A:I}*E_9+(g~.o90KeYD@2+VhsanWH@_<U;gE:YrDqEkHG7yud~>Hb@' );
define( 'LOGGED_IN_SALT',    '&esiA^nPb!^yvoVtQOs&L{HvWmGN/A8YzY  KJn!=dBjD)5u>1kS?VMDP@X=n.=K' );
define( 'NONCE_SALT',        'l<$]Dk5S^PXSx1np}hHI K$yKM!2vVXJUL+Ps;zNTA=bO/Y0_?|v~Qy[45Gr?#D(' );
define( 'WP_CACHE_KEY_SALT', 'm!0j6$(O%oo?v<,-9|&aKVgZ9n^>OEmr5E%.,qxOMV-oM=g8WCR:M7Qn4;fK$s|P' );

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';




/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';

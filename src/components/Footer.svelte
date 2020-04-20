<footer>
    <div class="footer-links">
        <div class="stack">
            <a href="">GNU General Public License</a>
            <a href="">File a GitHub feature request or issue</a>
        </div>
        <figure>
            <img
                    class="logo"
                    alt="BetaNYC Logo"
                    src="images/BetaNYC_short_white_on_blue.png"
            />
            <figcaption class="logo_caption">A <a href="https://beta.nyc/" target="_blank">BetaNYC</a> Tool</figcaption>
        </figure>
        <div class="stack">
            <p>Using <a href="http://geosearch.planninglabs.nyc/">GeoSearch 0.2</a>, PAD 19A</p>
            <p>A cybernetically enhanced <a href="https://svelte.dev/">Svelete</a> app</p>
        </div>

    </div>
</footer>

<style>
    footer {
        text-align: center;
        margin-top: 1rem;
    }

    .logo {
        width: 30px;
        margin: auto;
        display: block;
    }

    .logo_caption {
        font-size: 0.6rem;
        margin-top: 5px;
        text-align: center;
    }

    .footer-links {
        display: flex;
        font-size: 11px;
        justify-content: space-around;
    }

    .stack {
        display: flex;
        flex-direction: column;
    }
</style>
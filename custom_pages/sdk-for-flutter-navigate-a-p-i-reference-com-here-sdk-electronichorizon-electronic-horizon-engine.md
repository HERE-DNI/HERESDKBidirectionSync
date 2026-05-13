---
title: "ElectronicHorizonEngine"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-electronichorizon-electronic-horizon-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>ElectronicHorizonEngine</title>
    <link href="../../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../../";</script>
    <script>document.documentElement.classList.replace("no-js","js");</script>
    <script>const storage = localStorage.getItem("dokka-dark-mode")
    if (storage == null) {
        const osDarkSchemePreferred = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
        if (osDarkSchemePreferred === true) {
            document.getElementsByTagName("html")[0].classList.add("theme-dark")
        }
    } else {
        const savedDarkMode = JSON.parse(storage)
        if(savedDarkMode === true) {
            document.getElementsByTagName("html")[0].classList.add("theme-dark")
        }
    }
    </script>
<script type="text/javascript" src="https://unpkg.com/kotlin-playground@1/dist/playground.min.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../../styles/style.css" rel="Stylesheet">
<link href="../../../styles/main.css" rel="Stylesheet">
<link href="../../../styles/prism.css" rel="Stylesheet">
<link href="../../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="../../../index.html">
                    API Reference
            </a>
        <button class="navigation-controls--btn navigation-controls--btn_toc ui-kit_mobile-only" id="toc-toggle"
                type="button">Toggle table of contents
        </button>
        <div class="navigation-controls--break ui-kit_mobile-only"></div>
        <div class="library-version" id="library-version">
        </div>
        <div class="navigation-controls">
        <div class="filter-section filter-section_loading" id="filter-section">
                <button class="platform-tag platform-selector jvm-like" data-active=""
                        data-filter=":modules:dokkaHtml/release">androidJvm</button>
            <div class="dropdown filter-section--dropdown" data-role="dropdown" id="filter-section-dropdown">
                <button class="button button_dropdown filter-section--dropdown-toggle" role="combobox"
                        data-role="dropdown-toggle"
                        aria-controls="platform-tags-listbox"
                        aria-haspopup="listbox"
                        aria-expanded="false"
                        aria-label="Toggle source sets"
                ></button>
                <ul role="listbox" id="platform-tags-listbox" class="dropdown--list" data-role="dropdown-listbox">
                    <div class="dropdown--header"><span>Platform filter</span>
                        <button class="button" data-role="dropdown-toggle" aria-label="Close platform filter">
                            <i class="ui-kit-icon ui-kit-icon_cross"></i>
                        </button>
                    </div>
                        <li role="option" class="dropdown--option platform-selector-option jvm-like" tabindex="0">
                            <label class="checkbox">
                                <input type="checkbox" class="checkbox--input" id=":modules:dokkaHtml/release"
                                       data-filter=":modules:dokkaHtml/release"/>
                                <span class="checkbox--icon"></span>
                                androidJvm
                            </label>
                        </li>
                </ul>
                <div class="dropdown--overlay"></div>
            </div>
        </div>
            <button class="navigation-controls--btn navigation-controls--btn_theme" id="theme-toggle-button"
                    type="button">Switch theme
            </button>
            <div class="navigation-controls--btn navigation-controls--btn_search" id="searchBar" role="button">Search in
                API
            </div>
        </div>
    </nav>
        <div id="container">
            <div class="sidebar" id="leftColumn">
                <div class="dropdown theme-dark_mobile" data-role="dropdown" id="toc-dropdown">
                    <ul role="listbox" id="toc-listbox" class="dropdown--list dropdown--list_toc-list"
                        data-role="dropdown-listbox">
                        <div class="dropdown--header">
                            <span>
                                    API Reference
                            </span>
                            <button class="button" data-role="dropdown-toggle" aria-label="Close table of contents">
                                <i class="ui-kit-icon ui-kit-icon_cross"></i>
                            </button>
                        </div>
                        <div class="sidebar--inner" id="sideMenu"></div>
                    </ul>
                    <div class="dropdown--overlay"></div>
                </div>
            </div>
            <div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.electronichorizon/ElectronicHorizonEngine///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.electronichorizon</a><span class="delimiter">/</span><span class="current">ElectronicHorizonEngine</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Electronic</span><wbr></wbr><span>Horizon</span><wbr></wbr><span><span>Engine</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">ElectronicHorizonEngine</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Provides an electronic horizon engine that continuously predicts the road network ahead of the vehicle by using detailed map data, including road topography that is currently out of sight. You can subscribe to electronic horizon updates based on position updates by using <a href="../-electronic-horizon-listener/index.html">com.here.sdk.electronichorizon.ElectronicHorizonListener</a>. For more information about sub path levels, see <a href="../-electronic-horizon-options/look-ahead-distances-in-meters.html">com.here.sdk.electronichorizon.ElectronicHorizonOptions.lookAheadDistancesInMeters</a>.</p><p class="paragraph">The electronic horizon engine uses map-matched locations and can optionally use a <a href="../../com.here.sdk.routing/-route/index.html">com.here.sdk.routing.Route</a> to improve the most-preferred path (MPP).</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-739731457%2FConstructors%2F1617540583" anchor-label="ElectronicHorizonEngine" id="-739731457%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-electronic-horizon-engine.html"><span>Electronic</span><wbr></wbr><span>Horizon</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-739731457%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-electronic-horizon-options/index.html">ElectronicHorizonOptions</a><span class="token punctuation">, </span></span><span class="parameter ">transportMode<span class="token operator">: </span><a href="../../com.here.sdk.transport/-transport-mode/index.html">TransportMode</a><span class="token punctuation">, </span></span><span class="parameter ">route<span class="token operator">: </span><a href="../../com.here.sdk.routing/-route/index.html">Route</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of <a href="index.html">com.here.sdk.electronichorizon.ElectronicHorizonEngine</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-757276025%2FClasslikes%2F1617540583" anchor-label="Companion" id="-757276025%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-757276025%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-18117481%2FProperties%2F1617540583" anchor-label="route" id="-18117481%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="route.html"><span><span>route</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-18117481%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="route.html">route</a><span class="token operator">: </span><a href="../../com.here.sdk.routing/-route/index.html">Route</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The instance of <a href="../../com.here.sdk.routing/-route/index.html">com.here.sdk.routing.Route</a> that is being used by <a href="index.html">com.here.sdk.electronichorizon.ElectronicHorizonEngine</a>. You can override this property to rebuild the electronic horizon based on a different route.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-56527415%2FFunctions%2F1617540583" anchor-label="addElectronicHorizonListener" id="-56527415%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-electronic-horizon-listener.html"><span>add</span><wbr></wbr><span>Electronic</span><wbr></wbr><span>Horizon</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-56527415%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-electronic-horizon-listener.html"><span class="token function">addElectronicHorizonListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">electronicHorizonListener<span class="token operator">: </span><a href="../-electronic-horizon-listener/index.html">ElectronicHorizonListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds an <a href="../-electronic-horizon-listener/index.html">com.here.sdk.electronichorizon.ElectronicHorizonListener</a> to the subscription list.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="173185938%2FFunctions%2F1617540583" anchor-label="removeElectronicHorizonListener" id="173185938%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-electronic-horizon-listener.html"><span>remove</span><wbr></wbr><span>Electronic</span><wbr></wbr><span>Horizon</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="173185938%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove-electronic-horizon-listener.html"><span class="token function">removeElectronicHorizonListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">electronicHorizonListener<span class="token operator">: </span><a href="../-electronic-horizon-listener/index.html">ElectronicHorizonListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes an <a href="../-electronic-horizon-listener/index.html">com.here.sdk.electronichorizon.ElectronicHorizonListener</a> from the subscription list.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1924140513%2FFunctions%2F1617540583" anchor-label="update" id="-1924140513%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="update.html"><span><span>update</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1924140513%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="update.html"><span class="token function">update</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapMatchedLocation<span class="token operator">: </span><a href="../../com.here.sdk.navigation/-map-matched-location/index.html">MapMatchedLocation</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Updates the electronic horizon paths based on the provided map-matched location. This method returns immediately and does not block. When internal calculation is complete, callbacks are called on the main thread. When multiple updates are triggered while processing is still running, intermediate locations are skipped and only the last location is processed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
    <div class="footer">
        <a href="#content" id="go-to-top-link" class="footer--button footer--button_go-to-top"></a>
        <span>© 2026 Copyright</span>
        <span class="pull-right">
            <span>Generated by </span>
            <a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
                <span>dokka</span>
            </a>
        </span>
    </div>
            </div>
        </div>
    </div>
</body>
</html>
</div>
`
}</HTMLBlock>

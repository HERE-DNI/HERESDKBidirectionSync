---
title: "VenueService"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-venue-service-venue-service"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>VenueService</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.venue.service/VenueService///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.venue.service</a><span class="delimiter">/</span><span class="current">VenueService</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Venue</span><wbr></wbr><span><span>Service</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">VenueService</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Offers methods to download venues. Use of this object does not necessitate Map involvement.</p><p>
Before loading the venues, initialize the venue service
with one of the start methods.
</p>
<p>
The venue service is online only. Even if there is a cached
venue on the device, the venue service requires an online
connection to check if the venue is available for the user.
</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-624026545%2FClasslikes%2F1617540583" anchor-label="Companion" id="-624026545%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-624026545%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1448325856%2FClasslikes%2F1617540583" anchor-label="VenueOptionalFeature" id="-1448325856%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-venue-optional-feature/index.html"><span>Venue</span><wbr></wbr><span>Optional</span><wbr></wbr><span><span>Feature</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1448325856%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-venue-optional-feature/index.html">VenueOptionalFeature</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-venue-optional-feature/index.html">VenueService.VenueOptionalFeature</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Optional features enum</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-1156331846%2FProperties%2F1617540583" anchor-label="language" id="-1156331846%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="language.html"><span><span>language</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1156331846%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="language.html">language</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">The active language. The venue service will try to load a venue with a translation in the active language. If such translation doesn't exist, a venue will be loaded in its default language.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="79705933%2FProperties%2F1617540583" anchor-label="languages" id="79705933%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="languages.html"><span><span>languages</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="79705933%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="languages.html">languages</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">The languages available in the venue service.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="109913704%2FFunctions%2F1617540583" anchor-label="add" id="109913704%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add.html"><span><span>add</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="109913704%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add.html"><span class="token function">add</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-listener/index.html">VenueListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a venue . The is not added if it is <code class="lang-kotlin">null</code> or is already present in the list of .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add.html"><span class="token function">add</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-map-listener/index.html">VenueMapListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a venue map . The is not added if it is <code class="lang-kotlin">null</code> or is already present in the list of .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add.html"><span class="token function">add</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-service-listener/index.html">VenueServiceListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a service . The is not added if it is <code class="lang-kotlin">null</code> or is already present in the list of .</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="544624502%2FFunctions%2F1617540583" anchor-label="addVenueToLoad" id="544624502%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-venue-to-load.html"><span>add</span><wbr></wbr><span>Venue</span><wbr></wbr><span>To</span><wbr></wbr><span><span>Load</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="544624502%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-venue-to-load.html"><span class="token function">addVenueToLoad</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">venueId<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-venue-to-load.html"><span class="token function">addVenueToLoad</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">venueIdentifier<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a venue to the loading queue.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="109988720%2FFunctions%2F1617540583" anchor-label="getInitStatus" id="109988720%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-init-status.html"><span>get</span><wbr></wbr><span>Init</span><wbr></wbr><span><span>Status</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="109988720%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-init-status.html"><span class="token function">getInitStatus</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-venue-service-init-status/index.html">VenueServiceInitStatus</a></div><div class="brief "><p class="paragraph">Gets an initialization status.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-308817538%2FFunctions%2F1617540583" anchor-label="isInitialized" id="-308817538%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-initialized.html"><span>is</span><wbr></wbr><span><span>Initialized</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-308817538%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="is-initialized.html"><span class="token function">isInitialized</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Checks if the venue service is initialized.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="945341023%2FFunctions%2F1617540583" anchor-label="loadOptionalFeatures" id="945341023%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-optional-features.html"><span>load</span><wbr></wbr><span>Optional</span><wbr></wbr><span><span>Features</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="945341023%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="load-optional-features.html"><span class="token function">loadOptionalFeatures</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">optionalFeatureList<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="-venue-optional-feature/index.html">VenueService.VenueOptionalFeature</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Lets user load optional features for current session.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2005920223%2FFunctions%2F1617540583" anchor-label="loadTopologies" id="2005920223%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="load-topologies.html"><span>load</span><wbr></wbr><span><span>Topologies</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2005920223%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="load-topologies.html"><span class="token function">loadTopologies</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Lets user load topologies for current session</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-603676637%2FFunctions%2F1617540583" anchor-label="remove" id="-603676637%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove.html"><span><span>remove</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-603676637%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove.html"><span class="token function">remove</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-listener/index.html">VenueListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a venue . The is not removed if it is not present in the list of .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove.html"><span class="token function">remove</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-map-listener/index.html">VenueMapListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a venue map . The is not removed if it is not present in the list of .</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove.html"><span class="token function">remove</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="../-venue-service-listener/index.html">VenueServiceListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes a service . The is not removed if it is not present in the list of .</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1933844820%2FFunctions%2F1617540583" anchor-label="setHrn" id="1933844820%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-hrn.html"><span>set</span><wbr></wbr><span><span>Hrn</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1933844820%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-hrn.html"><span class="token function">setHrn</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">hrn<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets HRN of platform catalog.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-430794942%2FFunctions%2F1617540583" anchor-label="setLabeltextPreference" id="-430794942%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-labeltext-preference.html"><span>set</span><wbr></wbr><span>Labeltext</span><wbr></wbr><span><span>Preference</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-430794942%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-labeltext-preference.html"><span class="token function">setLabeltextPreference</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">labelTextPref<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets override labelTextPreference for labels.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-852166704%2FFunctions%2F1617540583" anchor-label="stop" id="-852166704%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="stop.html"><span><span>stop</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-852166704%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="stop.html"><span class="token function">stop</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Stops the venue service.</p></div></div></div>
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

---
title: "LocationManager"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapmatcher-location-manager"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>LocationManager</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapmatcher/LocationManager///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapmatcher</a><span class="delimiter">/</span><span class="current">LocationManager</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Location</span><wbr></wbr><span><span>Manager</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">LocationManager</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a>, <a href="../../com.here.sdk.core/-location-listener/index.html">LocationListener</a></div><p class="paragraph">LocationManager listens to position updates and provides the map-matched location using the LocationManagerListener.</p><p class="paragraph"><strong>Note:</strong> This is a <strong>beta</strong> release of this feature. There may be bugs and unexpected behaviors. Related APIs may change in future releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="19561279%2FConstructors%2F1617540583" anchor-label="LocationManager" id="19561279%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-location-manager.html"><span>Location</span><wbr></wbr><span><span>Manager</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="19561279%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of <a href="index.html">com.here.sdk.mapmatcher.LocationManager</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1376548209%2FClasslikes%2F1617540583" anchor-label="Companion" id="-1376548209%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1376548209%2FClasslikes%2F1617540583"></span>
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
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="1406686722%2FFunctions%2F1617540583" anchor-label="addMatchedLocationListener" id="1406686722%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-matched-location-listener.html"><span>add</span><wbr></wbr><span>Matched</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1406686722%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-matched-location-listener.html"><span class="token function">addMatchedLocationListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">matchedLocationListener<span class="token operator">: </span><a href="../-matched-location-listener/index.html">MatchedLocationListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds the <a href="../-matched-location-listener/index.html">com.here.sdk.mapmatcher.MatchedLocationListener</a> to the subscribtion list.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1002500414%2FFunctions%2F1617540583" anchor-label="onLocationUpdated" id="-1002500414%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-location-updated.html"><span>on</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Updated</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1002500414%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="on-location-updated.html"><span class="token function">onLocationUpdated</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">location<span class="token operator">: </span><a href="../../com.here.sdk.core/-location/index.html">Location</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Called each time a new location is available. In a navigation context while using the <code class="lang-kotlin">Navigator</code> or <code class="lang-kotlin">VisualNavigator</code>, it's required to set the <code class="lang-kotlin">Location.time</code> parameter for each <code class="lang-kotlin">Location</code> object so that the HERE SDK can map-match the locations properly. If the <code class="lang-kotlin">Location.time</code> parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the <code class="lang-kotlin">bearing</code> and <code class="lang-kotlin">speed</code> parameters for each <code class="lang-kotlin">Location</code> object. Invoked on the main thread.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-643119415%2FFunctions%2F1617540583" anchor-label="removeMatchedLocationListener" id="-643119415%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-matched-location-listener.html"><span>remove</span><wbr></wbr><span>Matched</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-643119415%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove-matched-location-listener.html"><span class="token function">removeMatchedLocationListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">matchedLocationListener<span class="token operator">: </span><a href="../-matched-location-listener/index.html">MatchedLocationListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes the <a href="../-matched-location-listener/index.html">com.here.sdk.mapmatcher.MatchedLocationListener</a> from the subscribtion list.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1581775068%2FFunctions%2F1617540583" anchor-label="setMapMatcher" id="1581775068%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-map-matcher.html"><span>set</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Matcher</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1581775068%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-map-matcher.html"><span class="token function">setMapMatcher</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapMatcher<span class="token operator">: </span><a href="../-map-matcher/index.html">MapMatcher</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets the <a href="../-map-matcher/index.html">com.here.sdk.mapmatcher.MapMatcher</a> for exclusive use by <a href="index.html">com.here.sdk.mapmatcher.LocationManager</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1804101525%2FFunctions%2F1617540583" anchor-label="takeMapMatcher" id="1804101525%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="take-map-matcher.html"><span>take</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Matcher</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1804101525%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="take-map-matcher.html"><span class="token function">takeMapMatcher</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-map-matcher/index.html">MapMatcher</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Retrieves and removes the <a href="../-map-matcher/index.html">com.here.sdk.mapmatcher.MapMatcher</a> from <a href="index.html">com.here.sdk.mapmatcher.LocationManager</a>. <strong>Note:</strong> After calling this method, <a href="index.html">com.here.sdk.mapmatcher.LocationManager</a> will no longer use the <a href="../-map-matcher/index.html">com.here.sdk.mapmatcher.MapMatcher</a> at all. the caller regains full ownership and responsibility for the <a href="../-map-matcher/index.html">com.here.sdk.mapmatcher.MapMatcher</a>.</p></div></div></div>
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

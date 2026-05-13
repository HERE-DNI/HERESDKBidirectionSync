---
title: "TrafficBroadcast"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-trafficbroadcast-traffic-broadcast"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>TrafficBroadcast</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.trafficbroadcast/TrafficBroadcast///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.trafficbroadcast</a><span class="delimiter">/</span><span class="current">TrafficBroadcast</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Traffic</span><wbr></wbr><span><span>Broadcast</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">TrafficBroadcast</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a>, <a href="../../com.here.sdk.core/-location-listener/index.html">LocationListener</a></div><p class="paragraph">A <code class="lang-kotlin">TrafficBroadcast</code> is expecting the <a href="https://en.wikipedia.org/wiki/Traffic_message_channel">RDS-TMC</a> format and it can be used when there is no internet connection, so that the <code class="lang-kotlin">OfflineRoutingEngine</code> can utilize traffic data coming over a radio channel. The <a href="activate.html">com.here.sdk.trafficbroadcast.TrafficBroadcast.activate</a> method needs to be called to receive traffic data events.</p><p class="paragraph"><strong>Note:</strong> In order to adopt the <code class="lang-kotlin">TrafficDataProvider</code> interface special hardware is required. Talk to your HERE representative for more details. Only by adopting the <code class="lang-kotlin">TrafficDataProvider</code> interface you can integrate radio station signals providing traffic broadcasts. Traffic broadcasts are meant to be used <i>independently</i> from the already included traffic on routes, on the map and from the HERE backends (when using the <code class="lang-kotlin">TrafficEngine</code>).</p><p class="paragraph">This class continuously reacts to new locations provided from a location source and acts as a <a href="../../com.here.sdk.core/-location-listener/index.html">com.here.sdk.core.LocationListener</a>. The location must be updated regardless of calling <a href="activate.html">com.here.sdk.trafficbroadcast.TrafficBroadcast.activate</a>.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="1631626846%2FConstructors%2F1617540583" anchor-label="TrafficBroadcast" id="1631626846%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-traffic-broadcast.html"><span>Traffic</span><wbr></wbr><span><span>Broadcast</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1631626846%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">parameters<span class="token operator">: </span><a href="../-traffic-broadcast-parameters/index.html">TrafficBroadcastParameters</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a><span class="token punctuation">, </span></span><span class="parameter ">parameters<span class="token operator">: </span><a href="../-traffic-broadcast-parameters/index.html">TrafficBroadcastParameters</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-579659735%2FClasslikes%2F1617540583" anchor-label="Companion" id="-579659735%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-579659735%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="-2006205110%2FProperties%2F1617540583" anchor-label="trafficDataProvider" id="-2006205110%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="traffic-data-provider.html"><span>traffic</span><wbr></wbr><span>Data</span><wbr></wbr><span><span>Provider</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2006205110%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="traffic-data-provider.html">trafficDataProvider</a><span class="token operator">: </span><a href="../../com.here.sdk.traffic/-traffic-data-provider/index.html">TrafficDataProvider</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The traffic data provider that provides the traffic information.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1716905371%2FFunctions%2F1617540583" anchor-label="activate" id="-1716905371%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="activate.html"><span><span>activate</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1716905371%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="activate.html"><span class="token function">activate</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Activates the reception of traffic data over the radio channel. This method is supposed to be called when the system loses internet connection, so that traffic data can be switched from the online source to the radio channel. When activation is done, requestTMCService is called from TMCServiceInterface</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="871710532%2FFunctions%2F1617540583" anchor-label="deactivate" id="871710532%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="deactivate.html"><span><span>deactivate</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="871710532%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="deactivate.html"><span class="token function">deactivate</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Deactivates the reception of traffic data over the radio channel. When deactivation is done, requestTMCService is called from TMCServiceInterface With special case of countryCode parameter = 0</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1812023844%2FFunctions%2F1617540583" anchor-label="onLocationUpdated" id="-1812023844%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-location-updated.html"><span>on</span><wbr></wbr><span>Location</span><wbr></wbr><span><span>Updated</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1812023844%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="on-location-updated.html"><span class="token function">onLocationUpdated</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">location<span class="token operator">: </span><a href="../../com.here.sdk.core/-location/index.html">Location</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Called each time a new location is available. In a navigation context while using the <code class="lang-kotlin">Navigator</code> or <code class="lang-kotlin">VisualNavigator</code>, it's required to set the <code class="lang-kotlin">Location.time</code> parameter for each <code class="lang-kotlin">Location</code> object so that the HERE SDK can map-match the locations properly. If the <code class="lang-kotlin">Location.time</code> parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the <code class="lang-kotlin">bearing</code> and <code class="lang-kotlin">speed</code> parameters for each <code class="lang-kotlin">Location</code> object. Invoked on the main thread.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1876526143%2FFunctions%2F1617540583" anchor-label="onTMCDataUpdated" id="-1876526143%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-t-m-c-data-updated.html"><span>on</span><wbr></wbr><span>TMCData</span><wbr></wbr><span><span>Updated</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1876526143%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="on-t-m-c-data-updated.html"><span class="token function">onTMCDataUpdated</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">tmcData<span class="token operator">: </span><a href="../-t-m-c-data/index.html">TMCData</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Must be called on every TMC data update.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1202158401%2FFunctions%2F1617540583" anchor-label="onTMCServiceProviderInfoUpdated" id="1202158401%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-t-m-c-service-provider-info-updated.html"><span>on</span><wbr></wbr><span>TMCService</span><wbr></wbr><span>Provider</span><wbr></wbr><span>Info</span><wbr></wbr><span><span>Updated</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1202158401%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="on-t-m-c-service-provider-info-updated.html"><span class="token function">onTMCServiceProviderInfoUpdated</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">tmcServiceProdiverInfo<span class="token operator">: </span><a href="../-t-m-c-service-provider-info/index.html">TMCServiceProviderInfo</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Must be called on every TMC service prodiver info update.</p></div></div></div>
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

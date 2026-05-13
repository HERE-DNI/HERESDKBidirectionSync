---
title: "com.here.sdk.core.engine"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-core-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>com.here.sdk.core.engine</title>
    <link href="../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../";</script>
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
<script type="text/javascript" src="../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../styles/style.css" rel="Stylesheet">
<link href="../../styles/main.css" rel="Stylesheet">
<link href="../../styles/prism.css" rel="Stylesheet">
<link href="../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
</head>
<body>
    <div class="root">
    <nav class="navigation theme-dark" id="navigation-wrapper">
            <a class="library-name--link" href="../../index.html">
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
<div class="main-content" data-page-type="package" id="content" pageIds="API Reference::com.here.sdk.core.engine////PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../index.html">API Reference</a><span class="delimiter">/</span><span class="current">com.here.sdk.core.engine</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>Package-level</span></span> <span><span>declarations</span></span></h1>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="TYPE">Types</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1613770931%2FClasslikes%2F1617540583" anchor-label="ApplicationUtilsInitializer" id="1613770931%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-application-utils-initializer/index.html"><span>Application</span><wbr></wbr><span>Utils</span><wbr></wbr><span><span>Initializer</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1613770931%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-application-utils-initializer/index.html">ApplicationUtilsInitializer</a></div><div class="brief "><p class="paragraph">This class is for internal use only.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1058604877%2FClasslikes%2F1617540583" anchor-label="AuthenticationMode" id="-1058604877%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-authentication-mode/index.html"><span>Authentication</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1058604877%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-authentication-mode/index.html">AuthenticationMode</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">This is a bearer authentication mode which adds or does not add a header (&quot;Authorization&quot;, &quot;Bearer $Token&quot;) to each online request of the module the object is added to. The token (if used) can be provided or is retrieved via key/secret from a dedicated backend.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="994549393%2FClasslikes%2F1617540583" anchor-label="CatalogConfiguration" id="994549393%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-catalog-configuration/index.html"><span>Catalog</span><wbr></wbr><span><span>Configuration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="994549393%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-catalog-configuration/index.html">CatalogConfiguration</a></div><div class="brief "><p class="paragraph">Using this class you can configure in the <a href="-s-d-k-options/index.html">com.here.sdk.core.engine.SDKOptions</a>, how the <a href="-s-d-k-native-engine/index.html">com.here.sdk.core.engine.SDKNativeEngine</a> should access, use and store the data for the desired catalog.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="144958674%2FClasslikes%2F1617540583" anchor-label="CatalogIdentifier" id="144958674%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-catalog-identifier/index.html"><span>Catalog</span><wbr></wbr><span><span>Identifier</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="144958674%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-catalog-identifier/index.html">CatalogIdentifier</a></div><div class="brief "><p class="paragraph">This class is used to identify any catalog in the HERE platform.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="200703713%2FClasslikes%2F1617540583" anchor-label="CatalogType" id="200703713%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-catalog-type/index.html"><span>Catalog</span><wbr></wbr><span><span>Type</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="200703713%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-catalog-type/index.html">CatalogType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-catalog-type/index.html">CatalogType</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Represents default HERE catalog types.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="439957928%2FClasslikes%2F1617540583" anchor-label="CatalogVersionHint" id="439957928%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-catalog-version-hint/index.html"><span>Catalog</span><wbr></wbr><span>Version</span><wbr></wbr><span><span>Hint</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="439957928%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-catalog-version-hint/index.html">CatalogVersionHint</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">This is a class for capturing user's intent for the desired catalog version to use in <a href="-desired-catalog/index.html">com.here.sdk.core.engine.DesiredCatalog</a> class.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-24198694%2FClasslikes%2F1617540583" anchor-label="CertificateSettings" id="-24198694%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-certificate-settings/index.html"><span>Certificate</span><wbr></wbr><span><span>Settings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-24198694%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-certificate-settings/index.html">CertificateSettings</a></div><div class="brief "><p class="paragraph">Certificate settings to be used by Curl+OpenSSL for authority</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1795419185%2FClasslikes%2F1617540583" anchor-label="DesiredCatalog" id="-1795419185%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-desired-catalog/index.html"><span>Desired</span><wbr></wbr><span><span>Catalog</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1795419185%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-desired-catalog/index.html">DesiredCatalog</a></div><div class="brief "><p class="paragraph">This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access. The user can specify the HERE Resource Name (HRN) for the catalog along with a hint for the desired version. If the desired version is not available, the HERE platform will determine the best version to use for a specific catalog or result in error logs. For information on how to specify the catalog version, see <a href="-catalog-version-hint/index.html">com.here.sdk.core.engine.CatalogVersionHint</a>. For information about catalogs and related concepts see <a href="-catalog-identifier/index.html">com.here.sdk.core.engine.CatalogIdentifier</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1857357032%2FClasslikes%2F1617540583" anchor-label="DeviceIdCallback" id="-1857357032%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-device-id-callback/index.html"><span>Device</span><wbr></wbr><span>Id</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1857357032%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-device-id-callback/index.html">DeviceIdCallback</a></div><div class="brief "><p class="paragraph">This method will be called on the main thread when <a href="-s-d-k-native-engine/get-device-id.html">com.here.sdk.core.engine.SDKNativeEngine.getDeviceId</a> has been completed.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-857339656%2FClasslikes%2F1617540583" anchor-label="EngineBaseURL" id="-857339656%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-engine-base-u-r-l/index.html"><span>Engine</span><wbr></wbr><span>Base</span><wbr></wbr><span><span>URL</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-857339656%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-engine-base-u-r-l/index.html">EngineBaseURL</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-engine-base-u-r-l/index.html">EngineBaseURL</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1726120136%2FClasslikes%2F1617540583" anchor-label="EngineOptions" id="-1726120136%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-engine-options/index.html"><span>Engine</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1726120136%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-engine-options/index.html">EngineOptions</a></div><div class="brief "><p class="paragraph">Specifies several options specific to different engines. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-18313975%2FClasslikes%2F1617540583" anchor-label="LayerConfiguration" id="-18313975%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-layer-configuration/index.html"><span>Layer</span><wbr></wbr><span><span>Configuration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-18313975%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-layer-configuration/index.html">LayerConfiguration</a></div><div class="brief "><p class="paragraph">A class to configure which layers should be enabled or disabled in the OCM map data. Disabling a layer allows to reduce the amount of data that will be downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1563127414%2FClasslikes%2F1617540583" anchor-label="LockingProcess" id="1563127414%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-locking-process/index.html"><span>Locking</span><wbr></wbr><span><span>Process</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1563127414%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-locking-process/index.html">LockingProcess</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">LockingProcess helps to detect situations when cache is locked with another process and attempt to create instance of <a href="-s-d-k-native-engine/index.html">com.here.sdk.core.engine.SDKNativeEngine</a> fails with error <a href="../com.here.sdk.core.errors/-instantiation-error-code/-f-a-i-l-e-d_-t-o_-l-o-c-k_-c-a-c-h-e_-f-o-l-d-e-r/index.html">com.here.sdk.core.errors.InstantiationErrorCode.FAILED_TO_LOCK_CACHE_FOLDER</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="860556329%2FClasslikes%2F1617540583" anchor-label="LogAppender" id="860556329%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-log-appender/index.html"><span>Log</span><wbr></wbr><span><span>Appender</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="860556329%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="-log-appender/index.html">LogAppender</a></div><div class="brief "><p class="paragraph">An interface to implement a listener to receive log messages.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1508207051%2FClasslikes%2F1617540583" anchor-label="LogControl" id="-1508207051%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-log-control/index.html"><span>Log</span><wbr></wbr><span><span>Control</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1508207051%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-log-control/index.html">LogControl</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">This class provides functionality to enable/disable console logs as well as setting a custom log appender to receive log messages from the SDK. Note, this class will load native libraries of SDK, therefore generally it should be used just before SDK initialization, otherwise, it might have an unexpected performance impact if called not at the right time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1921219026%2FClasslikes%2F1617540583" anchor-label="LogLevel" id="-1921219026%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-log-level/index.html"><span>Log</span><wbr></wbr><span><span>Level</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1921219026%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-log-level/index.html">LogLevel</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-log-level/index.html">LogLevel</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Severity levels for log messages.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="130773411%2FClasslikes%2F1617540583" anchor-label="NetworkSettings" id="130773411%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-network-settings/index.html"><span>Network</span><wbr></wbr><span><span>Settings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="130773411%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-network-settings/index.html">NetworkSettings</a></div><div class="brief "><p class="paragraph">Network configuration to be used by <a href="-s-d-k-native-engine/index.html">com.here.sdk.core.engine.SDKNativeEngine</a> during the initialization.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="479459308%2FClasslikes%2F1617540583" anchor-label="PassThroughFeature" id="479459308%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-pass-through-feature/index.html"><span>Pass</span><wbr></wbr><span>Through</span><wbr></wbr><span><span>Feature</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="479459308%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-pass-through-feature/index.html">PassThroughFeature</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-pass-through-feature/index.html">PassThroughFeature</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Represents features that are allowed to consume online data when the HERE SDK's offline mode is activated via <a href="-s-d-k-native-engine/is-offline-mode.html">com.here.sdk.core.engine.SDKNativeEngine.isOfflineMode</a> and/or <a href="-s-d-k-options/offline-mode.html">com.here.sdk.core.engine.SDKOptions.offlineMode</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="199810595%2FClasslikes%2F1617540583" anchor-label="ProxySettings" id="199810595%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-proxy-settings/index.html"><span>Proxy</span><wbr></wbr><span><span>Settings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="199810595%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-proxy-settings/index.html">ProxySettings</a></div><div class="brief "><p class="paragraph">Proxy configuration for the HERE SDK network that is applied per request. <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2133093316%2FClasslikes%2F1617540583" anchor-label="SDKBuildInformation" id="-2133093316%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-d-k-build-information/index.html"><span>SDKBuild</span><wbr></wbr><span><span>Information</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2133093316%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-s-d-k-build-information/index.html">SDKBuildInformation</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">The SDKBuildInformation class is designed to provide information about the SDK build.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1438982134%2FClasslikes%2F1617540583" anchor-label="SDKLogger" id="-1438982134%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-d-k-logger/index.html"><span><span>SDKLogger</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1438982134%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-s-d-k-logger/index.html">SDKLogger</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Logging interface for Android/iOS platforms. These logs are under management of <a href="-log-control/index.html">com.here.sdk.core.engine.LogControl</a> and should be used instead of platform-specific logging functions.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-663217727%2FClasslikes%2F1617540583" anchor-label="SDKNativeEngine" id="-663217727%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-d-k-native-engine/index.html"><span>SDKNative</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-663217727%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-s-d-k-native-engine/index.html">SDKNativeEngine</a> : <a href="../com.here/-native-base/index.html">NativeBase</a></div><div class="brief "><p class="paragraph">Holds internal services and configurations needed by various HERE SDK modules.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="604990730%2FClasslikes%2F1617540583" anchor-label="SDKOptions" id="604990730%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-d-k-options/index.html"><span><span>SDKOptions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="604990730%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-s-d-k-options/index.html">SDKOptions</a></div><div class="brief "><p class="paragraph">SDKOptions provide an alternative way to set or update the HERE SDK credentials and other parameters at runtime to initialize the <a href="-s-d-k-native-engine/index.html">com.here.sdk.core.engine.SDKNativeEngine</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="508718096%2FClasslikes%2F1617540583" anchor-label="SDKVersion" id="508718096%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-d-k-version/index.html"><span><span>SDKVersion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="508718096%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-s-d-k-version/index.html">SDKVersion</a></div><div class="brief "><p class="paragraph">The <code class="lang-kotlin">SDKVersion</code> represents version information for an SDK product. It encapsulates various attributes related to the version, including product variant, version details and backend configuration. Please note, <code class="lang-kotlin">sdk.core.engine.SDKBuildInformation</code> can be used to get <code class="lang-kotlin">SDKVersion</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1236654128%2FClasslikes%2F1617540583" anchor-label="UsageStats" id="-1236654128%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-usage-stats/index.html"><span>Usage</span><wbr></wbr><span><span>Stats</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1236654128%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-usage-stats/index.html">UsageStats</a></div><div class="brief "><p class="paragraph">A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.</p></div></div></div>
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

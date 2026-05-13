---
title: "WarnerEngine"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-warner-warner-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>WarnerEngine</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.warner/WarnerEngine///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.warner</a><span class="delimiter">/</span><span class="current">WarnerEngine</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Warner</span><wbr></wbr><span><span>Engine</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">WarnerEngine</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a>, <a href="../../com.here.sdk.electronichorizon/-electronic-horizon-listener/index.html">ElectronicHorizonListener</a></div><p class="paragraph">Provides the core functionality for generating and managing navigation warnings.</p><p class="paragraph"><code class="lang-kotlin">WarnerEngine</code> processes Electronic Horizon data and determines when various types of warnings should be issued. It is used with <a href="../../com.here.sdk.electronichorizon/-electronic-horizon-listener/index.html">com.here.sdk.electronichorizon.ElectronicHorizonListener</a>, which supply the road topology and positional updates required for warning evaluation.</p><p class="paragraph">The engine monitors enabled warning types and notifies registered listeners when new warnings become available.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="915968870%2FConstructors%2F1617540583" anchor-label="WarnerEngine" id="915968870%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-warner-engine.html"><span>Warner</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="915968870%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">enabledWarnings<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../../com.here.sdk.navigation/-warning-type/index.html">WarningType</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a><span class="token punctuation">, </span></span><span class="parameter ">enabledWarnings<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../../com.here.sdk.navigation/-warning-type/index.html">WarningType</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">sdkEngine<span class="token operator">: </span><a href="../../com.here.sdk.core.engine/-s-d-k-native-engine/index.html">SDKNativeEngine</a><span class="token punctuation">, </span></span><span class="parameter ">wallClock<span class="token operator">: </span><a href="../../com.here.sdk.navigation/-wall-clock/index.html">WallClock</a><span class="token punctuation">, </span></span><span class="parameter ">enabledWarnings<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../../com.here.sdk.navigation/-warning-type/index.html">WarningType</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="940820359%2FClasslikes%2F1617540583" anchor-label="Companion" id="940820359%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="940820359%2FClasslikes%2F1617540583"></span>
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
        <div class="table"><a data-name="1299890081%2FProperties%2F1617540583" anchor-label="timingProfile" id="1299890081%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="timing-profile.html"><span>timing</span><wbr></wbr><span><span>Profile</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1299890081%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="timing-profile.html">timingProfile</a><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-timing-profile/index.html">TimingProfile</a></div><div class="brief "><p class="paragraph">The timing profile that defines when navigation warnings should be triggered. Configures the base notification thresholds used for delivering navigation warnings. The effective thresholds depend on the selected <a href="../../com.here.sdk.navigation/-timing-profile/index.html">com.here.sdk.navigation.TimingProfile</a> and may adjust automatically according to the current speed limit:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="87832056%2FProperties%2F1617540583" anchor-label="warningOptions" id="87832056%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="warning-options.html"><span>warning</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="87832056%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="warning-options.html">warningOptions</a><span class="token operator">: </span><a href="../-warning-options/index.html">WarningOptions</a></div><div class="brief "><p class="paragraph">Options that define warning behavior for all the warners. Provides configuration parameters for all the warners.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="408964997%2FFunctions%2F1617540583" anchor-label="addCustomWarningProvider" id="408964997%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-custom-warning-provider.html"><span>add</span><wbr></wbr><span>Custom</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Provider</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="408964997%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-custom-warning-provider.html"><span class="token function">addCustomWarningProvider</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">customWarningProvider<span class="token operator">: </span><a href="../-custom-warning-provider/index.html">CustomWarningProvider</a><span class="token punctuation">, </span></span><span class="parameter ">segmentDataLoaderOptions<span class="token operator">: </span><a href="../../com.here.sdk.mapdata/-segment-data-loader-options/index.html">SegmentDataLoaderOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Registers a custom warning provider.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="682798512%2FFunctions%2F1617540583" anchor-label="addEnabledWarnings" id="682798512%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-enabled-warnings.html"><span>add</span><wbr></wbr><span>Enabled</span><wbr></wbr><span><span>Warnings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="682798512%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-enabled-warnings.html"><span class="token function">addEnabledWarnings</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningTypes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../../com.here.sdk.navigation/-warning-type/index.html">WarningType</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds the given warning types to the set of warnings monitored by the engine.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1087978467%2FFunctions%2F1617540583" anchor-label="addWarningListener" id="-1087978467%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="add-warning-listener.html"><span>add</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1087978467%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="add-warning-listener.html"><span class="token function">addWarningListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningListener<span class="token operator">: </span><a href="../-warning-listener/index.html">WarningListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Registers a listener that will receive warning notifications.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1239153500%2FFunctions%2F1617540583" anchor-label="clearCustomWarningProviders" id="1239153500%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="clear-custom-warning-providers.html"><span>clear</span><wbr></wbr><span>Custom</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Providers</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1239153500%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="clear-custom-warning-providers.html"><span class="token function">clearCustomWarningProviders</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Unregisters all custom warning providers.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1602892554%2FFunctions%2F1617540583" anchor-label="finalizeGivenWarnings" id="1602892554%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="finalize-given-warnings.html"><span>finalize</span><wbr></wbr><span>Given</span><wbr></wbr><span><span>Warnings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1602892554%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="finalize-given-warnings.html"><span class="token function">finalizeGivenWarnings</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Marks all currently active warnings as passed (<code class="lang-kotlin">DistanceType.PASSED</code>), notifies all registered <a href="../-warning-listener/index.html">com.here.sdk.warner.WarningListener</a> instances on the main thread, and then clears these warnings from their corresponding registries by invoking the appropriate<code class="lang-kotlin">WarningsRegistry.clear&lt;Type&gt;</code> methods.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="58345056%2FFunctions%2F1617540583" anchor-label="getCustomWarningNotificationDistances" id="58345056%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-custom-warning-notification-distances.html"><span>get</span><wbr></wbr><span>Custom</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="58345056%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-custom-warning-notification-distances.html"><span class="token function">getCustomWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">customWarningType<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-warning-notification-distances/index.html">WarningNotificationDistances</a></div><div class="brief "><p class="paragraph">Returns the warning notification distances for the specified custom warning type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1970866600%2FFunctions%2F1617540583" anchor-label="getEnabledWarnings" id="-1970866600%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-enabled-warnings.html"><span>get</span><wbr></wbr><span>Enabled</span><wbr></wbr><span><span>Warnings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1970866600%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-enabled-warnings.html"><span class="token function">getEnabledWarnings</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../../com.here.sdk.navigation/-warning-type/index.html">WarningType</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns the current list of enabled warning types. If the WarnerEngine was retrieved from the <code class="lang-kotlin">Navigator</code>, it will also contain all the warnings enabled for which listeners are set.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-175376562%2FFunctions%2F1617540583" anchor-label="getWarningNotificationDistances" id="-175376562%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-warning-notification-distances.html"><span>get</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-175376562%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-warning-notification-distances.html"><span class="token function">getWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningType<span class="token operator">: </span><a href="../../com.here.sdk.navigation/-warning-type/index.html">WarningType</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.navigation/-warning-notification-distances/index.html">WarningNotificationDistances</a></div><div class="brief "><p class="paragraph">Returns the warning notification distances for the requested warning type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1092925590%2FFunctions%2F1617540583" anchor-label="getWarningsRegistry" id="1092925590%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-warnings-registry.html"><span>get</span><wbr></wbr><span>Warnings</span><wbr></wbr><span><span>Registry</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1092925590%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-warnings-registry.html"><span class="token function">getWarningsRegistry</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-warnings-registry/index.html">WarningsRegistry</a></div><div class="brief "><p class="paragraph">Returns the centralized access point for retrieving full metadata of any supported warning category (e.g., safety cameras, truck restrictions, etc.). <a href="../-warnings-registry/index.html">com.here.sdk.warner.WarningsRegistry</a> class exposes getter methods, each returning the detailed warning object for the given identifier. Use this getter to look up complete warning information by its id, as provided through <code class="lang-kotlin">WarningListener.onWarning</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="51187170%2FFunctions%2F1617540583" anchor-label="onElectronicHorizonUpdated" id="51187170%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="on-electronic-horizon-updated.html"><span>on</span><wbr></wbr><span>Electronic</span><wbr></wbr><span>Horizon</span><wbr></wbr><span><span>Updated</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="51187170%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">external override </span><span class="token keyword">fun </span><a href="on-electronic-horizon-updated.html"><span class="token function">onElectronicHorizonUpdated</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">errorCode<span class="token operator">: </span><a href="../../com.here.sdk.electronichorizon/-electronic-horizon-error-code/index.html">ElectronicHorizonErrorCode</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">update<span class="token operator">: </span><a href="../../com.here.sdk.electronichorizon/-electronic-horizon-update/index.html">ElectronicHorizonUpdate</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Called whenever the electronic horizon subsystem produces:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="150306804%2FFunctions%2F1617540583" anchor-label="removeCustomWarningProvider" id="150306804%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-custom-warning-provider.html"><span>remove</span><wbr></wbr><span>Custom</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Provider</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="150306804%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove-custom-warning-provider.html"><span class="token function">removeCustomWarningProvider</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">customWarningProvider<span class="token operator">: </span><a href="../-custom-warning-provider/index.html">CustomWarningProvider</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Unregisters a custom warning provider.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1986250809%2FFunctions%2F1617540583" anchor-label="removeEnabledWarnings" id="1986250809%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-enabled-warnings.html"><span>remove</span><wbr></wbr><span>Enabled</span><wbr></wbr><span><span>Warnings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1986250809%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove-enabled-warnings.html"><span class="token function">removeEnabledWarnings</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningTypes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../../com.here.sdk.navigation/-warning-type/index.html">WarningType</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes the given warning types from the set of warnings monitored by the engine.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-899118732%2FFunctions%2F1617540583" anchor-label="removeWarningListener" id="-899118732%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="remove-warning-listener.html"><span>remove</span><wbr></wbr><span>Warning</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-899118732%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="remove-warning-listener.html"><span class="token function">removeWarningListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningListener<span class="token operator">: </span><a href="../-warning-listener/index.html">WarningListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Unregisters a previously added warning listener.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1430737311%2FFunctions%2F1617540583" anchor-label="setCustomWarningNotificationDistances" id="1430737311%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-custom-warning-notification-distances.html"><span>set</span><wbr></wbr><span>Custom</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1430737311%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-custom-warning-notification-distances.html"><span class="token function">setCustomWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">customWarningType<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a><span class="token punctuation">, </span></span><span class="parameter ">warningNotificationDistances<span class="token operator">: </span><a href="../../com.here.sdk.navigation/-warning-notification-distances/index.html">WarningNotificationDistances</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Sets the warning notification distances for the specified custom warning type.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1056529649%2FFunctions%2F1617540583" anchor-label="setEnabledWarnings" id="1056529649%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-enabled-warnings.html"><span>set</span><wbr></wbr><span>Enabled</span><wbr></wbr><span><span>Warnings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1056529649%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-enabled-warnings.html"><span class="token function">setEnabledWarnings</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningTypes<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../../com.here.sdk.navigation/-warning-type/index.html">WarningType</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Replaces the current set of enabled warning types with the provided list.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1373546023%2FFunctions%2F1617540583" anchor-label="setWarningNotificationDistances" id="-1373546023%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-warning-notification-distances.html"><span>set</span><wbr></wbr><span>Warning</span><wbr></wbr><span>Notification</span><wbr></wbr><span><span>Distances</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1373546023%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-warning-notification-distances.html"><span class="token function">setWarningNotificationDistances</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">warningType<span class="token operator">: </span><a href="../../com.here.sdk.navigation/-warning-type/index.html">WarningType</a><span class="token punctuation">, </span></span><span class="parameter ">warningNotificationDistances<span class="token operator">: </span><a href="../../com.here.sdk.navigation/-warning-notification-distances/index.html">WarningNotificationDistances</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Sets the warning notification distances for the specified warning type.</p></div></div></div>
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

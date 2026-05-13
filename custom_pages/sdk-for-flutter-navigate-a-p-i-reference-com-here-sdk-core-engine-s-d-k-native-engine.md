---
title: "SDKNativeEngine"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-core-engine-s-d-k-native-engine"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>SDKNativeEngine</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.core.engine/SDKNativeEngine///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.core.engine</a><span class="delimiter">/</span><span class="current">SDKNativeEngine</span></div>
  <div class="cover ">
    <h1 class="cover"><span>SDKNative</span><wbr></wbr><span><span>Engine</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">SDKNativeEngine</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Holds internal services and configurations needed by various HERE SDK modules.</p><p class="paragraph">You can initialize the HERE SDK in two ways:</p><ul><li><p class="paragraph">Create a shared instance of the <code class="lang-kotlin">SDKNativeEngine</code> with <code class="lang-kotlin">SDKNativeEngine.makeSharedInstance()</code>.</p></li><li><p class="paragraph">Create individual instances of the <code class="lang-kotlin">SDKNativeEngine</code> via <code class="lang-kotlin">SDKNativeEngine()</code>. Note that this does not automatically set a shared instance.</p></li></ul></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-545303909%2FConstructors%2F1617540583" anchor-label="SDKNativeEngine" id="-545303909%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-d-k-native-engine.html"><span>SDKNative</span><wbr></wbr><span><span>Engine</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-545303909%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">androidContext<span class="token operator">: </span><a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-s-d-k-options/index.html">SDKOptions</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Makes a new instance of SDKNativeEngine using supplied options.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1530542339%2FClasslikes%2F1617540583" anchor-label="Companion" id="1530542339%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1530542339%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1882292432%2FClasslikes%2F1617540583" anchor-label="PurgeMemoryStrategy" id="1882292432%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-purge-memory-strategy/index.html"><span>Purge</span><wbr></wbr><span>Memory</span><wbr></wbr><span><span>Strategy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1882292432%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-purge-memory-strategy/index.html">PurgeMemoryStrategy</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-purge-memory-strategy/index.html">SDKNativeEngine.PurgeMemoryStrategy</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Enum representing a strategy to flush memory caches.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-1090516704%2FProperties%2F1617540583" anchor-label="isOfflineMode" id="-1090516704%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="is-offline-mode.html"><span>is</span><wbr></wbr><span>Offline</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1090516704%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="is-offline-mode.html">isOfflineMode</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">The offline mode. Sets offline mode for the HERE SDK to offline or online. Defaults to false, which means the HERE SDK uses an online connection. When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set. See <a href="pass-through-features.html">com.here.sdk.core.engine.SDKNativeEngine.passThroughFeatures</a>. Note that the flag does not cancel pending requests. The mode can be enabled or disabled at any time. In order to fully operate offline, the mode needs to be enabled via <a href="../-s-d-k-options/offline-mode.html">com.here.sdk.core.engine.SDKOptions.offlineMode</a>. Initialization of the HERE SDK itself does not require an internet connection. Returns <code class="lang-kotlin">true</code> if the HERE SDK uses offline connection mode, otherwise returns <code class="lang-kotlin">false</code>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="535421598%2FProperties%2F1617540583" anchor-label="options" id="535421598%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="options.html"><span><span>options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="535421598%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="options.html">options</a><span class="token operator">: </span><a href="../-s-d-k-options/index.html">SDKOptions</a></div><div class="brief "><p class="paragraph">Options used by this instance of <a href="index.html">com.here.sdk.core.engine.SDKNativeEngine</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1082877003%2FProperties%2F1617540583" anchor-label="passThroughFeatures" id="1082877003%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="pass-through-features.html"><span>pass</span><wbr></wbr><span>Through</span><wbr></wbr><span><span>Features</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1082877003%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="pass-through-features.html">passThroughFeatures</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html">Set</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="../-pass-through-feature/index.html">PassThroughFeature</a><span class="token operator">&gt;</span><span class="token operator">?</span></div><div class="brief "><p class="paragraph">The pass through features. Sets pass through features which are allowed to use online data when HERE SDK is in offline mode. Pass through features can be updated at any time. When offline mode is disabled, existing pass through features will be removed. These needs to be set again when you enable offline mode next time. By default, reporting of HERE SDK <a href="../-usage-stats/index.html">com.here.sdk.core.engine.UsageStats</a> will be enabled when at least one pass-through feature is set.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="396143787%2FProperties%2F1617540583" anchor-label="proxySettings" id="396143787%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="proxy-settings.html"><span>proxy</span><wbr></wbr><span><span>Settings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="396143787%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="proxy-settings.html">proxySettings</a><span class="token operator">: </span><a href="../-proxy-settings/index.html">ProxySettings</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Proxy settings of this SDK engine that will be used by HERE SDK network for all requests. Defaults to (<code class="lang-kotlin">null</code>), which indicates proxy is not enabled. When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings. Pass (<code class="lang-kotlin">null</code>) to indicate that proxy should be disabled. If proxy is necessary from the start then it's recommended to use <a href="../-network-settings/proxy-settings.html">com.here.sdk.core.engine.NetworkSettings.proxySettings</a> in <a href="../-s-d-k-options/network-settings.html">com.here.sdk.core.engine.SDKOptions.networkSettings</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-264275996%2FProperties%2F1617540583" anchor-label="sdkUsageStats" id="-264275996%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-usage-stats.html"><span>sdk</span><wbr></wbr><span>Usage</span><wbr></wbr><span><span>Stats</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-264275996%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-usage-stats.html">sdkUsageStats</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="../-usage-stats/index.html">UsageStats</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Gets a list of usage statistics for all available HERE SDK features. <a href="../-usage-stats/index.html">com.here.sdk.core.engine.UsageStats</a> has cache and persistent storage. Reads from the persistent storage happen on <code class="lang-kotlin">SDKNativeEngine</code> creation step. Writes to persistent storage happen by reaching internal limit (amount of upload bytes, by default is 50KB).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1372492646%2FFunctions%2F1617540583" anchor-label="clearPersistentUsageStats" id="-1372492646%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="clear-persistent-usage-stats.html"><span>clear</span><wbr></wbr><span>Persistent</span><wbr></wbr><span>Usage</span><wbr></wbr><span><span>Stats</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1372492646%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="clear-persistent-usage-stats.html"><span class="token function">clearPersistentUsageStats</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Clear persistent storage for the HERE SDK <a href="../-usage-stats/index.html">com.here.sdk.core.engine.UsageStats</a>. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1830304167%2FFunctions%2F1617540583" anchor-label="clearUsageStatsCache" id="1830304167%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="clear-usage-stats-cache.html"><span>clear</span><wbr></wbr><span>Usage</span><wbr></wbr><span>Stats</span><wbr></wbr><span><span>Cache</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1830304167%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="clear-usage-stats-cache.html"><span class="token function">clearUsageStatsCache</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Clear cache for the HERE SDK <a href="../-usage-stats/index.html">com.here.sdk.core.engine.UsageStats</a>. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-659618243%2FFunctions%2F1617540583" anchor-label="dispose" id="-659618243%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="dispose.html"><span><span>dispose</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-659618243%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="dispose.html"><span class="token function">dispose</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Stops pending requests and closes open files and databases . Dispose signal is sent to dependent modules. Usage of engine, or dependent modules after calling dispose leads to undefined behavior. Please be aware that this method does not clean any type of storage. <strong>Note:</strong> This method should be called from main thread.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="97416482%2FFunctions%2F1617540583" anchor-label="enableUsageStats" id="97416482%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="enable-usage-stats.html"><span>enable</span><wbr></wbr><span>Usage</span><wbr></wbr><span><span>Stats</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="97416482%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="enable-usage-stats.html"><span class="token function">enableUsageStats</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">enabled<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Enable or disable <a href="../-usage-stats/index.html">com.here.sdk.core.engine.UsageStats</a> for the HERE SDK. Defaults to disabled (false). When enabled, <code class="lang-kotlin">SDKNativeEngine.getSdkUsageStats()</code> returns actual online data consumption. Note that the flag does not cancel pending requests. <a href="../-usage-stats/index.html">com.here.sdk.core.engine.UsageStats</a> can be enabled or disabled at any time.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1738808341%2FFunctions%2F1617540583" anchor-label="getDeviceId" id="1738808341%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="get-device-id.html"><span>get</span><wbr></wbr><span>Device</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1738808341%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="get-device-id.html"><span class="token function">getDeviceId</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">callback<span class="token operator">: </span><a href="../-device-id-callback/index.html">DeviceIdCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">The unique identifier assigned to the device for this application. This device ID is primarily used for tracking Monthly Active Users (MAUs).</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1926854115%2FFunctions%2F1617540583" anchor-label="purgeMemoryCaches" id="-1926854115%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="purge-memory-caches.html"><span>purge</span><wbr></wbr><span>Memory</span><wbr></wbr><span><span>Caches</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1926854115%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="purge-memory-caches.html"><span class="token function">purgeMemoryCaches</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">strategy<span class="token operator">: </span><a href="-purge-memory-strategy/index.html">SDKNativeEngine.PurgeMemoryStrategy</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Releases memory occupied by internal caches. Purging caches reduces memory footprint of application and may temporary reduce performance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="378071183%2FFunctions%2F1617540583" anchor-label="setAccessKeySecret" id="378071183%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-access-key-secret.html"><span>set</span><wbr></wbr><span>Access</span><wbr></wbr><span>Key</span><wbr></wbr><span><span>Secret</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="378071183%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-access-key-secret.html"><span class="token function">setAccessKeySecret</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">accessKeySecret<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Overrides HERE SDK access key secret with new value. The new credentials will be used for new requests.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-653524556%2FFunctions%2F1617540583" anchor-label="setAccessScope" id="-653524556%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="set-access-scope.html"><span>set</span><wbr></wbr><span>Access</span><wbr></wbr><span><span>Scope</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-653524556%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="set-access-scope.html"><span class="token function">setAccessScope</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">scope<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Overrides the token scope of the HERE SDK with new value. A new token will be fetched with the set scope and used for future requests. Setting an empty string will fetch a token for the global scope.</p></div></div></div>
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

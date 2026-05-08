---
title: "SDKOptions"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>SDKOptions</title>
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
            <a class="library-name--link" href="sdk-for-flutter-explore-index">
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.core.engine/SDKOptions///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine</a><span class="delimiter">/</span><span class="current">SDKOptions</span></div>
  <div class="cover ">
    <h1 class="cover"><span><span>SDKOptions</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">SDKOptions</a></div><p class="paragraph">SDKOptions provide an alternative way to set or update the HERE SDK credentials and other parameters at runtime to initialize the <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.SDKNativeEngine</a>.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-1167663628%2FConstructors%2F1617540583" anchor-label="SDKOptions" id="-1167663628%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-s-d-k-options"><span><span>SDKOptions</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1167663628%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">authenticationMode<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">AuthenticationMode</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs a SDKOptions from authentication mode. Other fields are filled with default values.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-1920760320%2FClasslikes%2F1617540583" anchor-label="ActionOnCacheLock" id="-1920760320%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Action</span><wbr></wbr><span>On</span><wbr></wbr><span>Cache</span><wbr></wbr><span><span>Lock</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1920760320%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="sdk-for-flutter-explore-index">ActionOnCacheLock</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">SDKOptions.ActionOnCacheLock</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Action on cache lock</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-247675636%2FClasslikes%2F1617540583" anchor-label="Companion" id="-247675636%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-247675636%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="-1889999315%2FProperties%2F1617540583" anchor-label="actionOnCacheLock" id="-1889999315%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-action-on-cache-lock"><span>action</span><wbr></wbr><span>On</span><wbr></wbr><span>Cache</span><wbr></wbr><span><span>Lock</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1889999315%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-action-on-cache-lock">actionOnCacheLock</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">SDKOptions.ActionOnCacheLock</a></div><div class="brief "><p class="paragraph">Specifies action to perform when cache folder is locked by another process. Default value is <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.SDKOptions.ActionOnCacheLock.WAIT_LOCKING_APP_FINISH</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1741877466%2FProperties%2F1617540583" anchor-label="authenticationMode" id="1741877466%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-authentication-mode"><span>authentication</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1741877466%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-authentication-mode">authenticationMode</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">AuthenticationMode</a></div><div class="brief "><p class="paragraph">Encapsulates Authentication method and parameters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1241869221%2FProperties%2F1617540583" anchor-label="autoUpdateOfOnlineCache" id="1241869221%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-auto-update-of-online-cache"><span>auto</span><wbr></wbr><span>Update</span><wbr></wbr><span>Of</span><wbr></wbr><span>Online</span><wbr></wbr><span><span>Cache</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1241869221%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-auto-update-of-online-cache">autoUpdateOfOnlineCache</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Parameter to enable automatic cache updates.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="736589430%2FProperties%2F1617540583" anchor-label="billingTag" id="736589430%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-billing-tag"><span>billing</span><wbr></wbr><span><span>Tag</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="736589430%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-billing-tag">billingTag</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Internal to HERE SDK. DO NOT USE THIS YET.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="156326622%2FProperties%2F1617540583" anchor-label="cachePath" id="156326622%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-cache-path"><span>cache</span><wbr></wbr><span><span>Path</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="156326622%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-cache-path">cachePath</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Path to be used for caching purposes. It should be a path to the desired location where the application has read/write permissions. The path can be on internal or external storage. By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths: <code class="lang-kotlin">Context.getCacheDir().getPath()</code> . If an absolute path is set, it will be used instead. If a relative path is set then directory <code class="lang-kotlin">Context.getCacheDir().getPath()</code> is used as parent path. Note, The cache path should be located under <a href="https://developer.android.com/training/data-storage/app-specific">app-specific directory</a>. Using shared directories such as <code class="lang-kotlin">Documents</code> is not recommended as it will expose HERE SDK files to the other apps. It will also require additional permissions such as <code class="lang-kotlin">MANAGE_EXTERNAL_STORAGE</code> and results in a poorer HERE SDK performance overall. The recommended location in terms of file I/O speed is the app's internal storage directory, whereas an external SD card is expected to be slower. This also depends on the quality of the used SD card.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="158772722%2FProperties%2F1617540583" anchor-label="cacheSizeInBytes" id="158772722%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-cache-size-in-bytes"><span>cache</span><wbr></wbr><span>Size</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Bytes</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="158772722%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-cache-size-in-bytes">cacheSizeInBytes</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a></div><div class="brief "><p class="paragraph">Desired upper bound of application size in bytes. When cached data exceeds cache_size, least recently used data will be removed. Default value 256MB</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-426554929%2FProperties%2F1617540583" anchor-label="catalogConfigurations" id="-426554929%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-catalog-configurations"><span>catalog</span><wbr></wbr><span><span>Configurations</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-426554929%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-catalog-configurations">catalogConfigurations</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="sdk-for-flutter-explore-index">CatalogConfiguration</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">This field specifies how the <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.SDKNativeEngine</a> should access, use and store data for different catalogs. You can access default catalogs on the HERE platform and also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases. For further information about catalogs and related concepts see <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.CatalogConfiguration</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1825923610%2FProperties%2F1617540583" anchor-label="customEngineOptions" id="1825923610%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-custom-engine-options"><span>custom</span><wbr></wbr><span>Engine</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1825923610%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-custom-engine-options">customEngineOptions</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="sdk-for-flutter-explore-index">EngineBaseURL</a><span class="token punctuation">, </span><a href="sdk-for-flutter-explore-index">EngineOptions</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Set custom options for SDK Engines. This includes:</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-264060296%2FProperties%2F1617540583" anchor-label="customOptions" id="-264060296%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-custom-options"><span>custom</span><wbr></wbr><span><span>Options</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-264060296%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-custom-options">customOptions</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Metadata</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Options that define custom behavior for the HERE SDK. These settings allow fine-tuning of internal thread pools and resource management for advanced use cases. These options are intended for <i>internal</i> usage only and should not be modified unless instructed by HERE support.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="46607014%2FProperties%2F1617540583" anchor-label="dataPath" id="46607014%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-data-path"><span>data</span><wbr></wbr><span><span>Path</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="46607014%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-data-path">dataPath</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Path used for storing application internal data, such as the offline search index and other essential data required for proper functionality.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1512798928%2FProperties%2F1617540583" anchor-label="layerConfiguration" id="-1512798928%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-layer-configuration"><span>layer</span><wbr></wbr><span><span>Configuration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1512798928%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-layer-configuration">layerConfiguration</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">LayerConfiguration</a></div><div class="brief "><p class="paragraph">Defines a list of data features that can be enabled / disabled. Once set to <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.SDKOptions</a> when a new HERE SDK is constructed, it will affect the map cache and offline maps. When disabling certain features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration</a>. However, for new map data, it will be applied. For offline maps, this <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration</a> can reduce the download size of all regions. Note that the <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration</a> is applied globally to all regions that will be downloaded in the future. It will not affect already downloaded regions. Updating a region will also not update the <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration</a>. Only the <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration</a> will be used that was set globally when a region was downloaded for the first time. If you want to update the <a href="sdk-for-flutter-explore-index">com.here.sdk.core.engine.LayerConfiguration</a> for an already downloaded region, please delete the region and download it again.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="6555149%2FProperties%2F1617540583" anchor-label="lowMemoryMode" id="6555149%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-low-memory-mode"><span>low</span><wbr></wbr><span>Memory</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="6555149%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-low-memory-mode">lowMemoryMode</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">If an application runs in a memory-constrained environment, enable this option to reduce the HERE SDK's memory footprint. When set to <code class="lang-kotlin">true</code> configures internal memory caches to consume less memory. Reduction in cache sizes also reduces performance of the HERE SDK. In order to release memory occupied by internal caches see <a href="sdk-for-flutter-explore-purge-memory-caches">com.here.sdk.core.engine.SDKNativeEngine.purgeMemoryCaches</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1931177356%2FProperties%2F1617540583" anchor-label="networkSettings" id="-1931177356%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-network-settings"><span>network</span><wbr></wbr><span><span>Settings</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1931177356%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-network-settings">networkSettings</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">NetworkSettings</a></div><div class="brief "><p class="paragraph">Network settings to use at the start. Some of those settings can be changed later.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="895456863%2FProperties%2F1617540583" anchor-label="offlineMode" id="895456863%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-offline-mode"><span>offline</span><wbr></wbr><span><span>Mode</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="895456863%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-offline-mode">offlineMode</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief "><p class="paragraph">Sets offline mode for the HERE SDK. Defaults to <code class="lang-kotlin">false</code>. When enabled, this prevents the HERE SDK from initiating any online connection from starting. The mode can be disabled or enabled again at any time via <a href="sdk-for-flutter-explore-is-offline-mode">com.here.sdk.core.engine.SDKNativeEngine.isOfflineMode</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="654392922%2FProperties%2F1617540583" anchor-label="persistentMapStoragePath" id="654392922%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-persistent-map-storage-path"><span>persistent</span><wbr></wbr><span>Map</span><wbr></wbr><span>Storage</span><wbr></wbr><span><span>Path</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="654392922%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-persistent-map-storage-path">persistentMapStoragePath</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Path to store persistent map data. This should be the a path to the desired location for which the application has read/write permissions. The path can be on internal or external storage. By default, this returns an empty string. Setting a new string, will overwrite the internally used default paths: <code class="lang-kotlin">Context.getFilesDir().getPath()</code> . If an absolute path is set, it will be used instead. If a relative path is set then directory <code class="lang-kotlin">Context.getFilesDir().getPath()</code> is used as parent path. <strong>Note</strong>: Offline maps stored at <code class="lang-kotlin">&lt;persistent_map_storage_path&gt;/v1/&lt;access_key_id&gt;/ocm-map/</code>, where <code class="lang-kotlin">&lt;access_key_id&gt;</code> is taken from <code class="lang-kotlin">SDKOptions.authenticationMode</code>. When <code class="lang-kotlin">SDKOptions</code> initialized with <code class="lang-kotlin">AuthenticationMode.withToken</code> or <code class="lang-kotlin">AuthenticationMode.withExternal</code>, then <code class="lang-kotlin">&lt;access_key_id&gt;</code> left empty.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1087482173%2FProperties%2F1617540583" anchor-label="politicalView" id="-1087482173%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-political-view"><span>political</span><wbr></wbr><span><span>View</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1087482173%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-political-view">politicalView</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Geopolitical view of a country, defined as a three letter country code by ISO 3166-1 alpha-3. Each disputed territory has an international and an alternative geopolitical view. When set, the map view will show all country boundaries according to the geopolitical view of the country that has been set.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1535574001%2FProperties%2F1617540583" anchor-label="scope" id="1535574001%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-scope"><span><span>scope</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1535574001%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">var </span><a href="sdk-for-flutter-explore-scope">scope</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief "><p class="paragraph">Optional project ID to set the project scope of the login session. Not used if empty. see also <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/manage-projects.html">Manage Projects</a> and <a href="https://www.here.com/docs/bundle/identity-and-access-management-developer-guide/page/topics/concepts.html">IAM Concepts</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="1483633772%2FFunctions%2F1617540583" anchor-label="equals" id="1483633772%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-equals"><span><span>equals</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1483633772%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">operator override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-equals"><span class="token function">equals</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">other<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a><span class="token operator">?</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1639500538%2FFunctions%2F1617540583" anchor-label="hashCode" id="1639500538%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-hash-code"><span>hash</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1639500538%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">override </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-hash-code"><span class="token function">hashCode</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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
`}</HTMLBlock>

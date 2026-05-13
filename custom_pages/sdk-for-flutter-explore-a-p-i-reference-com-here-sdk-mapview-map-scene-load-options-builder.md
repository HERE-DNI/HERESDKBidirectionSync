---
title: "MapSceneLoadOptionsBuilder"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-scene-load-options-builder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapSceneLoadOptionsBuilder</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapSceneLoadOptionsBuilder///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapSceneLoadOptionsBuilder</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span>Scene</span><wbr></wbr><span>Load</span><wbr></wbr><span>Options</span><wbr></wbr><span><span>Builder</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="index.html">MapSceneLoadOptionsBuilder</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Builder for creating <a href="../-map-scene-load-options/index.html">com.here.sdk.mapview.MapSceneLoadOptions</a> instances. This builder ensures that either a MapScheme or a configuration file is set, but not both.</p><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-575888031%2FConstructors%2F1617540583" anchor-label="MapSceneLoadOptionsBuilder" id="-575888031%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-map-scene-load-options-builder.html"><span>Map</span><wbr></wbr><span>Scene</span><wbr></wbr><span>Load</span><wbr></wbr><span>Options</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-575888031%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new builder instance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-2133573779%2FClasslikes%2F1617540583" anchor-label="Companion" id="-2133573779%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2133573779%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="-companion/index.html">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="298888225%2FClasslikes%2F1617540583" anchor-label="InstantiationErrorCode" id="298888225%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-instantiation-error-code/index.html"><span>Instantiation</span><wbr></wbr><span>Error</span><wbr></wbr><span><span>Code</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="298888225%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="-instantiation-error-code/index.html">InstantiationErrorCode</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="-instantiation-error-code/index.html">MapSceneLoadOptionsBuilder.InstantiationErrorCode</a><span class="token operator">&gt; </span></div><div class="brief "><p class="paragraph">Describes a reason for failing to build a <a href="../-map-scene-load-options/index.html">com.here.sdk.mapview.MapSceneLoadOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1937244718%2FClasslikes%2F1617540583" anchor-label="InstantiationErrorDetails" id="-1937244718%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-instantiation-error-details/index.html"><span>Instantiation</span><wbr></wbr><span>Error</span><wbr></wbr><span><span>Details</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1937244718%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-instantiation-error-details/index.html">InstantiationErrorDetails</a></div><div class="brief "><p class="paragraph">Describes the reason for failing to build a <a href="../-map-scene-load-options/index.html">com.here.sdk.mapview.MapSceneLoadOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="35545383%2FClasslikes%2F1617540583" anchor-label="InstantiationException" id="35545383%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-instantiation-exception/index.html"><span>Instantiation</span><wbr></wbr><span><span>Exception</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="35545383%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="-instantiation-exception/index.html">InstantiationException</a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span class="token keyword">val </span>error<span class="token operator">: </span><a href="-instantiation-error-details/index.html">MapSceneLoadOptionsBuilder.InstantiationErrorDetails</a></span></span><span class="token punctuation">)</span> : <a href="https://developer.android.com/reference/kotlin/java/lang/Exception.html">Exception</a></div><div class="brief "><p class="paragraph">Thrown when failing to build a <a href="../-map-scene-load-options/index.html">com.here.sdk.mapview.MapSceneLoadOptions</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-1642611720%2FFunctions%2F1617540583" anchor-label="build" id="-1642611720%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="build.html"><span><span>build</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1642611720%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="build.html"><span class="token function">build</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-map-scene-load-options/index.html">MapSceneLoadOptions</a></div><div class="brief "><p class="paragraph">Builds the <a href="../-map-scene-load-options/index.html">com.here.sdk.mapview.MapSceneLoadOptions</a> instance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="723365002%2FFunctions%2F1617540583" anchor-label="withConfigurationFile" id="723365002%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-configuration-file.html"><span>with</span><wbr></wbr><span>Configuration</span><wbr></wbr><span><span>File</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="723365002%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-configuration-file.html"><span class="token function">withConfigurationFile</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">configurationFile<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapSceneLoadOptionsBuilder</a></div><div class="brief "><p class="paragraph">Sets the configuration file path to load. Any map scheme set through <a href="with-map-scheme.html">com.here.sdk.mapview.MapSceneLoadOptionsBuilder.withMapScheme</a> will be discarded.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="446158559%2FFunctions%2F1617540583" anchor-label="withDisabledFeatures" id="446158559%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-disabled-features.html"><span>with</span><wbr></wbr><span>Disabled</span><wbr></wbr><span><span>Features</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="446158559%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-disabled-features.html"><span class="token function">withDisabledFeatures</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">disabledFeatures<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapSceneLoadOptionsBuilder</a></div><div class="brief "><p class="paragraph">Sets the features to disable in the new configuration.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1195177822%2FFunctions%2F1617540583" anchor-label="withEnabledFeatures" id="-1195177822%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-enabled-features.html"><span>with</span><wbr></wbr><span>Enabled</span><wbr></wbr><span><span>Features</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1195177822%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-enabled-features.html"><span class="token function">withEnabledFeatures</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">enabledFeatures<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token punctuation">, </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapSceneLoadOptionsBuilder</a></div><div class="brief "><p class="paragraph">Sets the features to enable in the new configuration.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="990036220%2FFunctions%2F1617540583" anchor-label="withMapScheme" id="990036220%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-map-scheme.html"><span>with</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Scheme</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="990036220%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-map-scheme.html"><span class="token function">withMapScheme</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">mapScheme<span class="token operator">: </span><a href="../-map-scheme/index.html">MapScheme</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapSceneLoadOptionsBuilder</a></div><div class="brief "><p class="paragraph">Sets the map scheme to load. Any configuration file set through <a href="with-configuration-file.html">com.here.sdk.mapview.MapSceneLoadOptionsBuilder.withConfigurationFile</a> will be discarded.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1601128913%2FFunctions%2F1617540583" anchor-label="withOverridingMapStyle" id="1601128913%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-overriding-map-style.html"><span>with</span><wbr></wbr><span>Overriding</span><wbr></wbr><span>Map</span><wbr></wbr><span><span>Style</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1601128913%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-overriding-map-style.html"><span class="token function">withOverridingMapStyle</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">overridingMapStyle<span class="token operator">: </span><a href="../-style/index.html">Style</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapSceneLoadOptionsBuilder</a></div><div class="brief "><p class="paragraph">Sets the style to override what is defined in the scene configuration.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1916253858%2FFunctions%2F1617540583" anchor-label="withWatermarkStyle" id="1916253858%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="with-watermark-style.html"><span>with</span><wbr></wbr><span>Watermark</span><wbr></wbr><span><span>Style</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1916253858%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="with-watermark-style.html"><span class="token function">withWatermarkStyle</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">watermarkStyle<span class="token operator">: </span><a href="../-watermark-style/index.html">WatermarkStyle</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">MapSceneLoadOptionsBuilder</a></div><div class="brief "><p class="paragraph">Sets the watermark style.</p></div></div></div>
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

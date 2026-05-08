---
title: "TruckBuilder"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>TruckBuilder</title>
    <link href="../../../../images/logo-icon.svg" rel="icon" type="image/svg">
    <script>var pathToRoot = "../../../../";</script>
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
<script type="text/javascript" src="../../../../scripts/sourceset_dependencies.js" async="async"></script>
<link href="../../../../styles/style.css" rel="Stylesheet">
<link href="../../../../styles/main.css" rel="Stylesheet">
<link href="../../../../styles/prism.css" rel="Stylesheet">
<link href="../../../../styles/logo-styles.css" rel="Stylesheet">
<link href="../../../../styles/font-jb-sans-auto.css" rel="Stylesheet">
<link href="../../../../ui-kit/ui-kit.min.css" rel="Stylesheet">
<script type="text/javascript" src="../../../../scripts/clipboard.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/navigation-loader.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/platform-content-handler.js" async="async"></script>
<script type="text/javascript" src="../../../../scripts/main.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/prism.js" async="async"></script>
<script type="text/javascript" src="../../../../ui-kit/ui-kit.min.js" defer="defer"></script>
<script type="text/javascript" src="../../../../scripts/symbol-parameters-wrapper_deferred.js" defer="defer"></script>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.transport/VehicleSpecification.TruckBuilder///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.transport</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">VehicleSpecification</a><span class="delimiter">/</span><span class="current">TruckBuilder</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Truck</span><wbr></wbr><span><span>Builder</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">TruckBuilder</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><p class="paragraph">This class constructs a <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.VehicleSpecification</a> for a truck.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="1639359706%2FConstructors%2F1617540583" anchor-label="TruckBuilder" id="1639359706%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-truck-builder"><span>Truck</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1639359706%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Creates a new instance of this class.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1838872491%2FClasslikes%2F1617540583" anchor-label="Companion" id="1838872491%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1838872491%2FClasslikes%2F1617540583"></span>
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
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="1427129142%2FFunctions%2F1617540583" anchor-label="build" id="1427129142%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-build"><span><span>build</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1427129142%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-build"><span class="token function">build</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification</a></div><div class="brief "><p class="paragraph">Builds the <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.VehicleSpecification</a> object for <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.TransportMode.TRUCK</a> with the specifications taken from the <a href="sdk-for-flutter-explore-index">com.here.sdk.transport.VehicleSpecification.TruckBuilder</a> object.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-370895863%2FFunctions%2F1617540583" anchor-label="withAxleCount" id="-370895863%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-axle-count"><span>with</span><wbr></wbr><span>Axle</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-370895863%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-axle-count"><span class="token function">withAxleCount</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">axleCount<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle axle count.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-247979895%2FFunctions%2F1617540583" anchor-label="withCurrentWeightInKilograms" id="-247979895%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-current-weight-in-kilograms"><span>with</span><wbr></wbr><span>Current</span><wbr></wbr><span>Weight</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-247979895%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-current-weight-in-kilograms"><span class="token function">withCurrentWeightInKilograms</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">currentWeightInKilograms<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle current weight in kilograms.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="623955741%2FFunctions%2F1617540583" anchor-label="withEmptyWeightInKilograms" id="623955741%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-empty-weight-in-kilograms"><span>with</span><wbr></wbr><span>Empty</span><wbr></wbr><span>Weight</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="623955741%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-empty-weight-in-kilograms"><span class="token function">withEmptyWeightInKilograms</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">emptyWeightInKilograms<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle empty weight in kilograms.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1844343899%2FFunctions%2F1617540583" anchor-label="withEngineSizeInCubicCentimeters" id="-1844343899%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-engine-size-in-cubic-centimeters"><span>with</span><wbr></wbr><span>Engine</span><wbr></wbr><span>Size</span><wbr></wbr><span>In</span><wbr></wbr><span>Cubic</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1844343899%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-engine-size-in-cubic-centimeters"><span class="token function">withEngineSizeInCubicCentimeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">engineSizeInCubicCentimeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle engine size in cubic centimeters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-476544364%2FFunctions%2F1617540583" anchor-label="withGrossWeightInKilograms" id="-476544364%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-gross-weight-in-kilograms"><span>with</span><wbr></wbr><span>Gross</span><wbr></wbr><span>Weight</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-476544364%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-gross-weight-in-kilograms"><span class="token function">withGrossWeightInKilograms</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">grossWeightInKilograms<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle gross weight in kilograms.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-840813131%2FFunctions%2F1617540583" anchor-label="withHazardousMaterials" id="-840813131%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-hazardous-materials"><span>with</span><wbr></wbr><span>Hazardous</span><wbr></wbr><span><span>Materials</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-840813131%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-hazardous-materials"><span class="token function">withHazardousMaterials</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">hazardousMaterials<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a><span class="token operator">&lt;</span><span><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html"><span class="token annotation builtin">JvmSuppressWildcards</span></a> </span><a href="sdk-for-flutter-explore-index">HazardousMaterial</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the hazardous materials transported in the vehicle.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="41269769%2FFunctions%2F1617540583" anchor-label="withHeightInCentimeters" id="41269769%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-height-in-centimeters"><span>with</span><wbr></wbr><span>Height</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="41269769%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-height-in-centimeters"><span class="token function">withHeightInCentimeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">heightInCentimeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle height in centimeters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1832210113%2FFunctions%2F1617540583" anchor-label="withIsCommercial" id="1832210113%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-is-commercial"><span>with</span><wbr></wbr><span>Is</span><wbr></wbr><span><span>Commercial</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1832210113%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-is-commercial"><span class="token function">withIsCommercial</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">isCommercial<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle is commercial flag.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="312075636%2FFunctions%2F1617540583" anchor-label="withIsTruckLight" id="312075636%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-is-truck-light"><span>with</span><wbr></wbr><span>Is</span><wbr></wbr><span>Truck</span><wbr></wbr><span><span>Light</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="312075636%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-is-truck-light"><span class="token function">withIsTruckLight</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">isTruckLight<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle truck light flag.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1130840758%2FFunctions%2F1617540583" anchor-label="withKingpinToRearAxleDistanceInCentimeters" id="-1130840758%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-kingpin-to-rear-axle-distance-in-centimeters"><span>with</span><wbr></wbr><span>Kingpin</span><wbr></wbr><span>To</span><wbr></wbr><span>Rear</span><wbr></wbr><span>Axle</span><wbr></wbr><span>Distance</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1130840758%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-kingpin-to-rear-axle-distance-in-centimeters"><span class="token function">withKingpinToRearAxleDistanceInCentimeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">length<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle kingpin to rear axle distance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-631968807%2FFunctions%2F1617540583" anchor-label="withLastCharacterOfLicensePlate" id="-631968807%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-last-character-of-license-plate"><span>with</span><wbr></wbr><span>Last</span><wbr></wbr><span>Character</span><wbr></wbr><span>Of</span><wbr></wbr><span>License</span><wbr></wbr><span><span>Plate</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-631968807%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-last-character-of-license-plate"><span class="token function">withLastCharacterOfLicensePlate</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lastCharacterOfLicensePlate<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle last character of the license plate.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1449178680%2FFunctions%2F1617540583" anchor-label="withLengthInCentimeters" id="-1449178680%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-length-in-centimeters"><span>with</span><wbr></wbr><span>Length</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1449178680%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-length-in-centimeters"><span class="token function">withLengthInCentimeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">lengthInCentimeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle length in centimeters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1642176507%2FFunctions%2F1617540583" anchor-label="withOccupancy" id="1642176507%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-occupancy"><span>with</span><wbr></wbr><span><span>Occupancy</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1642176507%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-occupancy"><span class="token function">withOccupancy</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">occupancy<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle occupants number.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1650710176%2FFunctions%2F1617540583" anchor-label="withPayloadCapacityInKilograms" id="1650710176%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-payload-capacity-in-kilograms"><span>with</span><wbr></wbr><span>Payload</span><wbr></wbr><span>Capacity</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1650710176%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-payload-capacity-in-kilograms"><span class="token function">withPayloadCapacityInKilograms</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">payloadCapacityInKilograms<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle payload capacity in kilograms.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="137464874%2FFunctions%2F1617540583" anchor-label="withTiresCount" id="137464874%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-tires-count"><span>with</span><wbr></wbr><span>Tires</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="137464874%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-tires-count"><span class="token function">withTiresCount</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">tiresCount<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle tires count.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="629764002%2FFunctions%2F1617540583" anchor-label="withTrailerAxleCount" id="629764002%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-trailer-axle-count"><span>with</span><wbr></wbr><span>Trailer</span><wbr></wbr><span>Axle</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="629764002%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-trailer-axle-count"><span class="token function">withTrailerAxleCount</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">trailerAxleCount<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle trailer axle count.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-769837422%2FFunctions%2F1617540583" anchor-label="withTrailerCount" id="-769837422%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-trailer-count"><span>with</span><wbr></wbr><span>Trailer</span><wbr></wbr><span><span>Count</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-769837422%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-trailer-count"><span class="token function">withTrailerCount</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">trailerCount<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle trailer count.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1170998246%2FFunctions%2F1617540583" anchor-label="withTruckCategory" id="-1170998246%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-truck-category"><span>with</span><wbr></wbr><span>Truck</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1170998246%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-truck-category"><span class="token function">withTruckCategory</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">truckCategory<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TruckCategory</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle truck category.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2142007528%2FFunctions%2F1617540583" anchor-label="withTunnelCategory" id="2142007528%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-tunnel-category"><span>with</span><wbr></wbr><span>Tunnel</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2142007528%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-tunnel-category"><span class="token function">withTunnelCategory</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">tunnelCategory<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">TunnelCategory</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle tunnel category.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1000137320%2FFunctions%2F1617540583" anchor-label="withWeightPerAxleGroup" id="1000137320%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-weight-per-axle-group"><span>with</span><wbr></wbr><span>Weight</span><wbr></wbr><span>Per</span><wbr></wbr><span>Axle</span><wbr></wbr><span><span>Group</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1000137320%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-weight-per-axle-group"><span class="token function">withWeightPerAxleGroup</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">weightPerAxleGroup<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">WeightPerAxleGroup</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle weight per axle group.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2013155661%2FFunctions%2F1617540583" anchor-label="withWeightPerAxleInKilograms" id="2013155661%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-weight-per-axle-in-kilograms"><span>with</span><wbr></wbr><span>Weight</span><wbr></wbr><span>Per</span><wbr></wbr><span>Axle</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Kilograms</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2013155661%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-weight-per-axle-in-kilograms"><span class="token function">withWeightPerAxleInKilograms</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">weightPerAxleInKilograms<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle weight per axle in kilograms.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1816595730%2FFunctions%2F1617540583" anchor-label="withWidthInCentimeters" id="-1816595730%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-with-width-in-centimeters"><span>with</span><wbr></wbr><span>Width</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Centimeters</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1816595730%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-with-width-in-centimeters"><span class="token function">withWidthInCentimeters</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">widthInCentimeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">VehicleSpecification.TruckBuilder</a></div><div class="brief "><p class="paragraph">Sets the vehicle width in centimeters.</p></div></div></div>
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

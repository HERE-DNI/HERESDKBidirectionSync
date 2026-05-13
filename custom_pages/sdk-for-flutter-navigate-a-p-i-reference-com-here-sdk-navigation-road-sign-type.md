---
title: "RoadSignType"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-navigation-road-sign-type"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>RoadSignType</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.navigation/RoadSignType///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.navigation</a><span class="delimiter">/</span><span class="current">RoadSignType</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Road</span><wbr></wbr><span>Sign</span><wbr></wbr><span><span>Type</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">enum </span><a href="index.html">RoadSignType</a> : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a><span class="token operator">&lt;</span><a href="index.html">RoadSignType</a><span class="token operator">&gt; </span></div><p class="paragraph">A road sign type classifying road signs that can appear along a road. Some signs are standardized and look the same in all countries, e.g. <a href="-s-t-o-p_-s-i-g-n/index.html">com.here.sdk.navigation.RoadSignType.STOP_SIGN</a>. In general, the visual appearance of the road signs can differ across countries. Some road signs can be combined with other signs, like <code class="lang-kotlin">WeatherType</code> signs. The road sign will be always shown topmost.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
    <div class="tabs-section-body">
      <div data-togglable="ENTRY">
        <h2 class="">Entries</h2>
        <div class="table"><a data-name="1873521469%2FClasslikes%2F1617540583" anchor-label="UNKNOWN" id="1873521469%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-u-n-k-n-o-w-n/index.html">UNKNOWN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1873521469%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-u-n-k-n-o-w-n/index.html">UNKNOWN</a></div></div><div class="brief "><p class="paragraph">Unknown road sign type</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="690159616%2FClasslikes%2F1617540583" anchor-label="START_OF_NO_OVERTAKING" id="690159616%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-t-a-r-t_-o-f_-n-o_-o-v-e-r-t-a-k-i-n-g/index.html">START_OF_NO_OVERTAKING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="690159616%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-t-a-r-t_-o-f_-n-o_-o-v-e-r-t-a-k-i-n-g/index.html">START_OF_NO_OVERTAKING</a></div></div><div class="brief "><p class="paragraph">A sign indicating the starting of a no overtaking zone. Example: <a href="https://en.wikipedia.org/wiki/Prohibitory_traffic_sign#No_overtaking_or_passing_signs">Start of no overtaking sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1209859417%2FClasslikes%2F1617540583" anchor-label="END_OF_NO_OVERTAKING" id="-1209859417%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-n-d_-o-f_-n-o_-o-v-e-r-t-a-k-i-n-g/index.html">END_OF_NO_OVERTAKING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1209859417%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-n-d_-o-f_-n-o_-o-v-e-r-t-a-k-i-n-g/index.html">END_OF_NO_OVERTAKING</a></div></div><div class="brief "><p class="paragraph">A sign indicating the ending of a no overtaking zone. Example: <a href="https://en.wikipedia.org/wiki/Prohibitory_traffic_sign#End_of_overtaking_signs">End of no overtaking sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2096476164%2FClasslikes%2F1617540583" anchor-label="PROTECTED_OVERTAKING_EXTRA_LANE" id="2096476164%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-o-t-e-c-t-e-d_-o-v-e-r-t-a-k-i-n-g_-e-x-t-r-a_-l-a-n-e/index.html">PROTECTED_OVERTAKING_EXTRA_LANE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2096476164%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-o-t-e-c-t-e-d_-o-v-e-r-t-a-k-i-n-g_-e-x-t-r-a_-l-a-n-e/index.html">PROTECTED_OVERTAKING_EXTRA_LANE</a></div></div><div class="brief "><p class="paragraph">A sign indicating an extra lane for overtaking. Example: <a href="https://en.wikipedia.org/wiki/Passing_lane#/media/File:MUTCD_R4-3.svg">Protected overtaking extra lane sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1043361091%2FClasslikes%2F1617540583" anchor-label="PROTECTED_OVERTAKING_EXTRA_LANE_RIGHT_SIDE" id="-1043361091%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-o-t-e-c-t-e-d_-o-v-e-r-t-a-k-i-n-g_-e-x-t-r-a_-l-a-n-e_-r-i-g-h-t_-s-i-d-e/index.html">PROTECTED_OVERTAKING_EXTRA_LANE_RIGHT_SIDE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1043361091%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-o-t-e-c-t-e-d_-o-v-e-r-t-a-k-i-n-g_-e-x-t-r-a_-l-a-n-e_-r-i-g-h-t_-s-i-d-e/index.html">PROTECTED_OVERTAKING_EXTRA_LANE_RIGHT_SIDE</a></div></div><div class="brief "><p class="paragraph">A sign indicating an extra lane for overtaking on the right side. Example: <a href="https://en.wikipedia.org/wiki/Passing_lane#/media/File:MUTCD_R4-16.svg">Protected overtaking extra lane on the right side sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1388657388%2FClasslikes%2F1617540583" anchor-label="PROTECTED_OVERTAKING_EXTRA_LANE_LEFT_SIDE" id="-1388657388%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-o-t-e-c-t-e-d_-o-v-e-r-t-a-k-i-n-g_-e-x-t-r-a_-l-a-n-e_-l-e-f-t_-s-i-d-e/index.html">PROTECTED_OVERTAKING_EXTRA_LANE_LEFT_SIDE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1388657388%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-o-t-e-c-t-e-d_-o-v-e-r-t-a-k-i-n-g_-e-x-t-r-a_-l-a-n-e_-l-e-f-t_-s-i-d-e/index.html">PROTECTED_OVERTAKING_EXTRA_LANE_LEFT_SIDE</a></div></div><div class="brief "><p class="paragraph">A sign indicating an extra lane for overtaking on the left side. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Australia#/media/File:Australia_road_sign_R6-29.svg">Protected overtaking extra lane on the left side sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1041249079%2FClasslikes%2F1617540583" anchor-label="LANE_MERGE_RIGHT" id="1041249079%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-a-n-e_-m-e-r-g-e_-r-i-g-h-t/index.html">LANE_MERGE_RIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1041249079%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-a-n-e_-m-e-r-g-e_-r-i-g-h-t/index.html">LANE_MERGE_RIGHT</a></div></div><div class="brief "><p class="paragraph">A sign indicating merging of the right lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W4-3R.svg">Merge right lane sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1524125228%2FClasslikes%2F1617540583" anchor-label="LANE_MERGE_LEFT" id="-1524125228%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-a-n-e_-m-e-r-g-e_-l-e-f-t/index.html">LANE_MERGE_LEFT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1524125228%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-a-n-e_-m-e-r-g-e_-l-e-f-t/index.html">LANE_MERGE_LEFT</a></div></div><div class="brief "><p class="paragraph">A sign indicating merging of the left lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Mauritius#/media/File:Mauritius_Road_Signs_-_Warning_Sign_-_Traffic_Merging_From_Left_Behind.svg">Merge left lane sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1220707486%2FClasslikes%2F1617540583" anchor-label="LANE_MERGE_CENTER" id="-1220707486%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-a-n-e_-m-e-r-g-e_-c-e-n-t-e-r/index.html">LANE_MERGE_CENTER</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1220707486%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-a-n-e_-m-e-r-g-e_-c-e-n-t-e-r/index.html">LANE_MERGE_CENTER</a></div></div><div class="brief "><p class="paragraph">A sign indicating merging of the center lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:Roadsign_lane_drop_ahead.svg">Merge center lane sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="970993064%2FClasslikes%2F1617540583" anchor-label="RAILWAY_CROSSING_PROTECTED" id="970993064%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-a-i-l-w-a-y_-c-r-o-s-s-i-n-g_-p-r-o-t-e-c-t-e-d/index.html">RAILWAY_CROSSING_PROTECTED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="970993064%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-a-i-l-w-a-y_-c-r-o-s-s-i-n-g_-p-r-o-t-e-c-t-e-d/index.html">RAILWAY_CROSSING_PROTECTED</a></div></div><div class="brief "><p class="paragraph">A sign indicating a protected railway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W7-4.svg">Protected railway crossing sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1243847535%2FClasslikes%2F1617540583" anchor-label="RAILWAY_CROSSING_UNPROTECTED" id="1243847535%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-a-i-l-w-a-y_-c-r-o-s-s-i-n-g_-u-n-p-r-o-t-e-c-t-e-d/index.html">RAILWAY_CROSSING_UNPROTECTED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1243847535%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-a-i-l-w-a-y_-c-r-o-s-s-i-n-g_-u-n-p-r-o-t-e-c-t-e-d/index.html">RAILWAY_CROSSING_UNPROTECTED</a></div></div><div class="brief "><p class="paragraph">A sign indicating an unprotected railway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W7-7-L.svg">Protected railway crossing sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1686023534%2FClasslikes%2F1617540583" anchor-label="ROAD_NARROWS" id="1686023534%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-o-a-d_-n-a-r-r-o-w-s/index.html">ROAD_NARROWS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1686023534%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-o-a-d_-n-a-r-r-o-w-s/index.html">ROAD_NARROWS</a></div></div><div class="brief "><p class="paragraph">A sign indicating a narrowing road. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W4-3.svg">Road narrows sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="672906625%2FClasslikes%2F1617540583" anchor-label="SHARP_CURVE_LEFT" id="672906625%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-h-a-r-p_-c-u-r-v-e_-l-e-f-t/index.html">SHARP_CURVE_LEFT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="672906625%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-h-a-r-p_-c-u-r-v-e_-l-e-f-t/index.html">SHARP_CURVE_LEFT</a></div></div><div class="brief "><p class="paragraph">A sign indicating a sharp curve to the left. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_512L.svg">Sharp curve left sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="429759786%2FClasslikes%2F1617540583" anchor-label="SHARP_CURVE_RIGHT" id="429759786%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-h-a-r-p_-c-u-r-v-e_-r-i-g-h-t/index.html">SHARP_CURVE_RIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="429759786%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-h-a-r-p_-c-u-r-v-e_-r-i-g-h-t/index.html">SHARP_CURVE_RIGHT</a></div></div><div class="brief "><p class="paragraph">A sign indicating a sharp curve to the right. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_512.svg">Sharp curve right sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="98782881%2FClasslikes%2F1617540583" anchor-label="WINDING_ROAD_STARTING_LEFT" id="98782881%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-w-i-n-d-i-n-g_-r-o-a-d_-s-t-a-r-t-i-n-g_-l-e-f-t/index.html">WINDING_ROAD_STARTING_LEFT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="98782881%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-w-i-n-d-i-n-g_-r-o-a-d_-s-t-a-r-t-i-n-g_-l-e-f-t/index.html">WINDING_ROAD_STARTING_LEFT</a></div></div><div class="brief "><p class="paragraph">A sign indicating a winding road starting left. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_513.svg">Winding road starting left sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-188207094%2FClasslikes%2F1617540583" anchor-label="WINDING_ROAD_STARTING_RIGHT" id="-188207094%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-w-i-n-d-i-n-g_-r-o-a-d_-s-t-a-r-t-i-n-g_-r-i-g-h-t/index.html">WINDING_ROAD_STARTING_RIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-188207094%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-w-i-n-d-i-n-g_-r-o-a-d_-s-t-a-r-t-i-n-g_-r-i-g-h-t/index.html">WINDING_ROAD_STARTING_RIGHT</a></div></div><div class="brief "><p class="paragraph">A sign indicating a winding road starting right. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_513R.svg">Winding road starting right sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1917953915%2FClasslikes%2F1617540583" anchor-label="START_OF_NO_OVERTAKING_TRUCKS" id="1917953915%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-t-a-r-t_-o-f_-n-o_-o-v-e-r-t-a-k-i-n-g_-t-r-u-c-k-s/index.html">START_OF_NO_OVERTAKING_TRUCKS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1917953915%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-t-a-r-t_-o-f_-n-o_-o-v-e-r-t-a-k-i-n-g_-t-r-u-c-k-s/index.html">START_OF_NO_OVERTAKING_TRUCKS</a></div></div><div class="brief "><p class="paragraph">A sign indicating no overtaking trucks. Example: <a href="https://en.wikipedia.org/wiki/File:Vorschriftszeichen_4c.svg">No overtaking trucks sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1372564212%2FClasslikes%2F1617540583" anchor-label="END_OF_NO_OVERTAKING_TRUCKS" id="1372564212%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-n-d_-o-f_-n-o_-o-v-e-r-t-a-k-i-n-g_-t-r-u-c-k-s/index.html">END_OF_NO_OVERTAKING_TRUCKS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1372564212%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-n-d_-o-f_-n-o_-o-v-e-r-t-a-k-i-n-g_-t-r-u-c-k-s/index.html">END_OF_NO_OVERTAKING_TRUCKS</a></div></div><div class="brief "><p class="paragraph">A sign indicating the end of no overtaking trucks zone. Example: <a href="https://en.wikipedia.org/wiki/File:Vorschriftszeichen_4d.svg">End of no overtaking trucks sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1350521059%2FClasslikes%2F1617540583" anchor-label="STEEP_HILL_UPWARDS" id="1350521059%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-t-e-e-p_-h-i-l-l_-u-p-w-a-r-d-s/index.html">STEEP_HILL_UPWARDS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1350521059%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-t-e-e-p_-h-i-l-l_-u-p-w-a-r-d-s/index.html">STEEP_HILL_UPWARDS</a></div></div><div class="brief "><p class="paragraph">A sign indicating a steep hill upwards. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-9(b).svg">Steep hills upwards sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="103529660%2FClasslikes%2F1617540583" anchor-label="STEEP_HILL_DOWNWARDS" id="103529660%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-t-e-e-p_-h-i-l-l_-d-o-w-n-w-a-r-d-s/index.html">STEEP_HILL_DOWNWARDS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="103529660%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-t-e-e-p_-h-i-l-l_-d-o-w-n-w-a-r-d-s/index.html">STEEP_HILL_DOWNWARDS</a></div></div><div class="brief "><p class="paragraph">A sign indicating a steep hill downward. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-9(a).svg">Steep hills downwards sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1358849235%2FClasslikes%2F1617540583" anchor-label="STOP_SIGN" id="-1358849235%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-t-o-p_-s-i-g-n/index.html">STOP_SIGN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1358849235%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-t-o-p_-s-i-g-n/index.html">STOP_SIGN</a></div></div><div class="brief "><p class="paragraph">A sign indicating a stop. Example: <a href="https://en.wikipedia.org/wiki/File:IE_road_sign_RUS-027.svg">Stop sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="978256293%2FClasslikes%2F1617540583" anchor-label="LATERAL_WIND" id="978256293%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-a-t-e-r-a-l_-w-i-n-d/index.html">LATERAL_WIND</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="978256293%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-a-t-e-r-a-l_-w-i-n-d/index.html">LATERAL_WIND</a></div></div><div class="brief "><p class="paragraph">A sign indicating lateral winds. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W5-226.svg">Lateral winds sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="345051500%2FClasslikes%2F1617540583" anchor-label="GENERAL_WARNING_SIGN" id="345051500%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-g-e-n-e-r-a-l_-w-a-r-n-i-n-g_-s-i-g-n/index.html">GENERAL_WARNING_SIGN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="345051500%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-g-e-n-e-r-a-l_-w-a-r-n-i-n-g_-s-i-g-n/index.html">GENERAL_WARNING_SIGN</a></div></div><div class="brief "><p class="paragraph">A sign indicating a general warning. Example: <a href="https://en.wikipedia.org/wiki/File:Hong_Kong_road_sign_240.svg">General warning sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1585100170%2FClasslikes%2F1617540583" anchor-label="RISK_OF_GROUNDING" id="-1585100170%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-r-i-s-k_-o-f_-g-r-o-u-n-d-i-n-g/index.html">RISK_OF_GROUNDING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1585100170%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-r-i-s-k_-o-f_-g-r-o-u-n-d-i-n-g/index.html">RISK_OF_GROUNDING</a></div></div><div class="brief "><p class="paragraph">A sign indicating risk of grounding. Example: <a href="https://en.wikipedia.org/wiki/File:Croatia_road_sign_A31.svg">Risk of grounding sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1996269035%2FClasslikes%2F1617540583" anchor-label="GENERAL_CURVE" id="1996269035%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-g-e-n-e-r-a-l_-c-u-r-v-e/index.html">GENERAL_CURVE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1996269035%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-g-e-n-e-r-a-l_-c-u-r-v-e/index.html">GENERAL_CURVE</a></div></div><div class="brief "><p class="paragraph">A sign indicating a general curve. Example: <a href="https://en.wikipedia.org/wiki/File:Italian_traffic_signs_-_curva_pericolosa_a_sinistra.svg">General curve sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="836031708%2FClasslikes%2F1617540583" anchor-label="END_OF_ALL_RESTRICTIONS" id="836031708%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-n-d_-o-f_-a-l-l_-r-e-s-t-r-i-c-t-i-o-n-s/index.html">END_OF_ALL_RESTRICTIONS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="836031708%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-n-d_-o-f_-a-l-l_-r-e-s-t-r-i-c-t-i-o-n-s/index.html">END_OF_ALL_RESTRICTIONS</a></div></div><div class="brief "><p class="paragraph">A sign indicating the end of all restrictions. Example: <a href="https://en.wikipedia.org/wiki/File:Estonia_road_sign_374.svg">End of all restrictions sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1013357747%2FClasslikes%2F1617540583" anchor-label="GENERAL_HILL" id="-1013357747%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-g-e-n-e-r-a-l_-h-i-l-l/index.html">GENERAL_HILL</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1013357747%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-g-e-n-e-r-a-l_-h-i-l-l/index.html">GENERAL_HILL</a></div></div><div class="brief "><p class="paragraph">A sign indicating a general hill. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W7-1A.svg">General hill sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1850252968%2FClasslikes%2F1617540583" anchor-label="ANIMAL_CROSSING" id="-1850252968%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-n-i-m-a-l_-c-r-o-s-s-i-n-g/index.html">ANIMAL_CROSSING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1850252968%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-n-i-m-a-l_-c-r-o-s-s-i-n-g/index.html">ANIMAL_CROSSING</a></div></div><div class="brief "><p class="paragraph">A sign indicating animal crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Gefahrenzeichen_13b.svg">Animal crossing sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-865630163%2FClasslikes%2F1617540583" anchor-label="ICY_CONDITIONS" id="-865630163%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-i-c-y_-c-o-n-d-i-t-i-o-n-s/index.html">ICY_CONDITIONS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-865630163%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-i-c-y_-c-o-n-d-i-t-i-o-n-s/index.html">ICY_CONDITIONS</a></div></div><div class="brief "><p class="paragraph">A sign indicating icy conditions. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-185.png">Icy conditions sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2121147222%2FClasslikes%2F1617540583" anchor-label="SLIPPERY_ROAD" id="2121147222%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-l-i-p-p-e-r-y_-r-o-a-d/index.html">SLIPPERY_ROAD</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2121147222%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-l-i-p-p-e-r-y_-r-o-a-d/index.html">SLIPPERY_ROAD</a></div></div><div class="brief "><p class="paragraph">A sign indicating slippery road. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-12.svg">Slippery road sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1546866551%2FClasslikes%2F1617540583" anchor-label="FALLING_ROCKS" id="-1546866551%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-a-l-l-i-n-g_-r-o-c-k-s/index.html">FALLING_ROCKS</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1546866551%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-a-l-l-i-n-g_-r-o-c-k-s/index.html">FALLING_ROCKS</a></div></div><div class="brief "><p class="paragraph">A sign indicating falling rocks. Example: <a href="https://en.wikipedia.org/wiki/File:Moldova_road_sign_1.25.2.svg">Falling rocks sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="908103786%2FClasslikes%2F1617540583" anchor-label="SCHOOL_ZONE" id="908103786%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-s-c-h-o-o-l_-z-o-n-e/index.html">SCHOOL_ZONE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="908103786%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-s-c-h-o-o-l_-z-o-n-e/index.html">SCHOOL_ZONE</a></div></div><div class="brief "><p class="paragraph">A sign indicating school zone. Example: <a href="https://en.wikipedia.org/wiki/File:Mauritius_Road_Signs_-_Warning_Sign_-_Children.svg">School zone sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="610737073%2FClasslikes%2F1617540583" anchor-label="TRAMWAY_CROSSING" id="610737073%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-r-a-m-w-a-y_-c-r-o-s-s-i-n-g/index.html">TRAMWAY_CROSSING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="610737073%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-r-a-m-w-a-y_-c-r-o-s-s-i-n-g/index.html">TRAMWAY_CROSSING</a></div></div><div class="brief "><p class="paragraph">A sign indicating a tramway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W5-41.svg">Tramway crossing sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2063670141%2FClasslikes%2F1617540583" anchor-label="CONGESTION_HAZARD" id="2063670141%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-c-o-n-g-e-s-t-i-o-n_-h-a-z-a-r-d/index.html">CONGESTION_HAZARD</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2063670141%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-c-o-n-g-e-s-t-i-o-n_-h-a-z-a-r-d/index.html">CONGESTION_HAZARD</a></div></div><div class="brief "><p class="paragraph">A sign indicating congestion hazard. Example: <a href="https://en.wikipedia.org/wiki/File:Czech_Republic_road_sign_A_23.svg">Congestion hazard sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-987786667%2FClasslikes%2F1617540583" anchor-label="ACCIDENT_HAZARD" id="-987786667%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-a-c-c-i-d-e-n-t_-h-a-z-a-r-d/index.html">ACCIDENT_HAZARD</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-987786667%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-a-c-c-i-d-e-n-t_-h-a-z-a-r-d/index.html">ACCIDENT_HAZARD</a></div></div><div class="brief "><p class="paragraph">A sign indicating accident hazard. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_France#/media/File:France_road_sign_AK31.svg">Accident hazard sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1690658019%2FClasslikes%2F1617540583" anchor-label="PRIORITY_OVER_ONCOMING_TRAFFIC" id="1690658019%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-r-i-o-r-i-t-y_-o-v-e-r_-o-n-c-o-m-i-n-g_-t-r-a-f-f-i-c/index.html">PRIORITY_OVER_ONCOMING_TRAFFIC</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1690658019%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-r-i-o-r-i-t-y_-o-v-e-r_-o-n-c-o-m-i-n-g_-t-r-a-f-f-i-c/index.html">PRIORITY_OVER_ONCOMING_TRAFFIC</a></div></div><div class="brief "><p class="paragraph">A sign indicating priority over oncoming traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Zeichen_308_-_Vorrang_vor_dem_Gegenverkehr,_StVO_1992.svg">Priority over oncoming traffic sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1427853757%2FClasslikes%2F1617540583" anchor-label="YIELD_TO_ONCOMING_TRAFFIC" id="-1427853757%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-y-i-e-l-d_-t-o_-o-n-c-o-m-i-n-g_-t-r-a-f-f-i-c/index.html">YIELD_TO_ONCOMING_TRAFFIC</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1427853757%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-y-i-e-l-d_-t-o_-o-n-c-o-m-i-n-g_-t-r-a-f-f-i-c/index.html">YIELD_TO_ONCOMING_TRAFFIC</a></div></div><div class="brief "><p class="paragraph">A sign indicating yielding to oncoming traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Moldova_road_sign_2.5.svg">Yield to oncoming traffic sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="778643339%2FClasslikes%2F1617540583" anchor-label="CROSSING_WITH_PRIORITY_FROM_THE_RIGHT" id="778643339%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-c-r-o-s-s-i-n-g_-w-i-t-h_-p-r-i-o-r-i-t-y_-f-r-o-m_-t-h-e_-r-i-g-h-t/index.html">CROSSING_WITH_PRIORITY_FROM_THE_RIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="778643339%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-c-r-o-s-s-i-n-g_-w-i-t-h_-p-r-i-o-r-i-t-y_-f-r-o-m_-t-h-e_-r-i-g-h-t/index.html">CROSSING_WITH_PRIORITY_FROM_THE_RIGHT</a></div></div><div class="brief "><p class="paragraph">A sign indicating crossing with priority from the right. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_France#/media/File:France_road_sign_AB1.svg">Crossing with priority from the right sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-77190215%2FClasslikes%2F1617540583" anchor-label="PEDESTRIAN_CROSSING" id="-77190215%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-p-e-d-e-s-t-r-i-a-n_-c-r-o-s-s-i-n-g/index.html">PEDESTRIAN_CROSSING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-77190215%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-p-e-d-e-s-t-r-i-a-n_-c-r-o-s-s-i-n-g/index.html">PEDESTRIAN_CROSSING</a></div></div><div class="brief "><p class="paragraph">A sign indicating pedestrian crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Estonia_road_sign_171.svg">Pedestrian crossing sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="42390272%2FClasslikes%2F1617540583" anchor-label="YIELD" id="42390272%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-y-i-e-l-d/index.html">YIELD</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="42390272%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-y-i-e-l-d/index.html">YIELD</a></div></div><div class="brief "><p class="paragraph">A sign indicating yielding. Example: <a href="https://en.wikipedia.org/wiki/File:Ontario_Wb-1A.svg">Yield sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1211820326%2FClasslikes%2F1617540583" anchor-label="DOUBLE_HAIRPIN" id="-1211820326%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-d-o-u-b-l-e_-h-a-i-r-p-i-n/index.html">DOUBLE_HAIRPIN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1211820326%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-d-o-u-b-l-e_-h-a-i-r-p-i-n/index.html">DOUBLE_HAIRPIN</a></div></div><div class="brief "><p class="paragraph">A sign indicating a double hairpin. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Australia#/media/File:Australia_road_sign_W1-7-L.svg">Double hairpin sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-190809689%2FClasslikes%2F1617540583" anchor-label="TRIPLE_HAIRPIN" id="-190809689%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-r-i-p-l-e_-h-a-i-r-p-i-n/index.html">TRIPLE_HAIRPIN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-190809689%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-r-i-p-l-e_-h-a-i-r-p-i-n/index.html">TRIPLE_HAIRPIN</a></div></div><div class="brief "><p class="paragraph">A sign indicating a triple hairpin. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_doppia_curva_sx.svg">Triple hairpin sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1108234487%2FClasslikes%2F1617540583" anchor-label="EMBANKMENT" id="1108234487%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-m-b-a-n-k-m-e-n-t/index.html">EMBANKMENT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1108234487%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-m-b-a-n-k-m-e-n-t/index.html">EMBANKMENT</a></div></div><div class="brief "><p class="paragraph">A sign indicating embankment. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-138.png">Embankment sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="12981997%2FClasslikes%2F1617540583" anchor-label="TWO_WAY_TRAFFIC" id="12981997%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-w-o_-w-a-y_-t-r-a-f-f-i-c/index.html">TWO_WAY_TRAFFIC</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="12981997%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-w-o_-w-a-y_-t-r-a-f-f-i-c/index.html">TWO_WAY_TRAFFIC</a></div></div><div class="brief "><p class="paragraph">A sign indicating two way traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Gefahrenzeichen_14.svg">Two way traffic sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-954020561%2FClasslikes%2F1617540583" anchor-label="URBAN_AREA" id="-954020561%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-u-r-b-a-n_-a-r-e-a/index.html">URBAN_AREA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-954020561%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-u-r-b-a-n_-a-r-e-a/index.html">URBAN_AREA</a></div></div><div class="brief "><p class="paragraph">A sign indicating urban area. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_preavviso_intersezione.svg">Urban area sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1530250677%2FClasslikes%2F1617540583" anchor-label="HUMP_BRIDGE" id="-1530250677%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-u-m-p_-b-r-i-d-g-e/index.html">HUMP_BRIDGE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1530250677%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-u-m-p_-b-r-i-d-g-e/index.html">HUMP_BRIDGE</a></div></div><div class="brief "><p class="paragraph">A sign indicating a hump bridge. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_Kingdom#/media/File:UK_traffic_sign_528.svg">Hump bridge sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-399250241%2FClasslikes%2F1617540583" anchor-label="UNEVEN_ROAD" id="-399250241%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-u-n-e-v-e-n_-r-o-a-d/index.html">UNEVEN_ROAD</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-399250241%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-u-n-e-v-e-n_-r-o-a-d/index.html">UNEVEN_ROAD</a></div></div><div class="brief "><p class="paragraph">A sign indicating uneven road. Example: <a href="https://en.wikipedia.org/wiki/File:IE_road_sign_W-133.svg">Uneven road sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-518371837%2FClasslikes%2F1617540583" anchor-label="FLOOD_AREA" id="-518371837%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-f-l-o-o-d_-a-r-e-a/index.html">FLOOD_AREA</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-518371837%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-f-l-o-o-d_-a-r-e-a/index.html">FLOOD_AREA</a></div></div><div class="brief "><p class="paragraph">A sign indicating a flood area. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_zona_soggetta_ad_allagamento.svg">Flood area sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="591501508%2FClasslikes%2F1617540583" anchor-label="OBSTACLE" id="591501508%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-o-b-s-t-a-c-l-e/index.html">OBSTACLE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="591501508%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-o-b-s-t-a-c-l-e/index.html">OBSTACLE</a></div></div><div class="brief "><p class="paragraph">A sign indicating an obstacle. Example: <a href="https://en.wikipedia.org/wiki/Warning_sign#/media/File:Belgian_road_sign_A51.svg">Obstacle sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-458145268%2FClasslikes%2F1617540583" anchor-label="HORN_SIGN" id="-458145268%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-h-o-r-n_-s-i-g-n/index.html">HORN_SIGN</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-458145268%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-h-o-r-n_-s-i-g-n/index.html">HORN_SIGN</a></div></div><div class="brief "><p class="paragraph">A sign indicating restriction for horning. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-355.png">Horn sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="752222495%2FClasslikes%2F1617540583" anchor-label="NO_ENGINE_BRAKE" id="752222495%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o_-e-n-g-i-n-e_-b-r-a-k-e/index.html">NO_ENGINE_BRAKE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="752222495%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o_-e-n-g-i-n-e_-b-r-a-k-e/index.html">NO_ENGINE_BRAKE</a></div></div><div class="brief "><p class="paragraph">A sign indicating no engine brake. Example: <a href="https://commons.wikimedia.org/wiki/File:Canada_Avoid_Engine_Brake_Sign.svg">No engine brake sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1722575581%2FClasslikes%2F1617540583" anchor-label="END_OF_NO_ENGINE_BRAKE" id="1722575581%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-n-d_-o-f_-n-o_-e-n-g-i-n-e_-b-r-a-k-e/index.html">END_OF_NO_ENGINE_BRAKE</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1722575581%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-n-d_-o-f_-n-o_-e-n-g-i-n-e_-b-r-a-k-e/index.html">END_OF_NO_ENGINE_BRAKE</a></div></div><div class="brief "><p class="paragraph">A sign indicating the end of no engine brake zone. Example: No examples available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1256052834%2FClasslikes%2F1617540583" anchor-label="NO_IDLING" id="1256052834%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o_-i-d-l-i-n-g/index.html">NO_IDLING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1256052834%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o_-i-d-l-i-n-g/index.html">NO_IDLING</a></div></div><div class="brief "><p class="paragraph">A sign indicating no idling. Example: <a href="https://en.wikipedia.org/wiki/Idle_reduction#/media/File:Idle_free_zone_-_turn_engine_off_sign.jpg">No idling sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1513423674%2FClasslikes%2F1617540583" anchor-label="TRUCK_ROLLOVER" id="-1513423674%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-r-u-c-k_-r-o-l-l-o-v-e-r/index.html">TRUCK_ROLLOVER</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1513423674%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-r-u-c-k_-r-o-l-l-o-v-e-r/index.html">TRUCK_ROLLOVER</a></div></div><div class="brief "><p class="paragraph">A sign indicating truck rollover. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W1-13L.svg">Truck rollover sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="135452847%2FClasslikes%2F1617540583" anchor-label="LOW_GEAR" id="135452847%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-l-o-w_-g-e-a-r/index.html">LOW_GEAR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="135452847%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-l-o-w_-g-e-a-r/index.html">LOW_GEAR</a></div></div><div class="brief "><p class="paragraph">A sign indicating the use of low gear. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_Philippines#/media/File:Philippines_road_sign_S1-3.svg">Low gear sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1701890225%2FClasslikes%2F1617540583" anchor-label="END_OF_LOW_GEAR" id="1701890225%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-e-n-d_-o-f_-l-o-w_-g-e-a-r/index.html">END_OF_LOW_GEAR</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1701890225%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-e-n-d_-o-f_-l-o-w_-g-e-a-r/index.html">END_OF_LOW_GEAR</a></div></div><div class="brief "><p class="paragraph">A sign indicating the use of low gear. Example: No examples available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="538012919%2FClasslikes%2F1617540583" anchor-label="BICYCLE_CROSSING" id="538012919%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-b-i-c-y-c-l-e_-c-r-o-s-s-i-n-g/index.html">BICYCLE_CROSSING</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="538012919%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-b-i-c-y-c-l-e_-c-r-o-s-s-i-n-g/index.html">BICYCLE_CROSSING</a></div></div><div class="brief "><p class="paragraph">A sign indicating bicycles crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W6-7-FYG.svg">Bicycle crossing sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1213500903%2FClasslikes%2F1617540583" anchor-label="YIELD_TO_BICYCLES" id="-1213500903%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-y-i-e-l-d_-t-o_-b-i-c-y-c-l-e-s/index.html">YIELD_TO_BICYCLES</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1213500903%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-y-i-e-l-d_-t-o_-b-i-c-y-c-l-e-s/index.html">YIELD_TO_BICYCLES</a></div></div><div class="brief "><p class="paragraph">A sign indicating yielding to bicycles. Example: <a href="https://en.wikipedia.org/wiki/File:MK_road_sign_302.2.svg">Yield to bicycles sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1499613554%2FClasslikes%2F1617540583" anchor-label="NO_TOWED_CARAVAN_ALLOWED" id="1499613554%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o_-t-o-w-e-d_-c-a-r-a-v-a-n_-a-l-l-o-w-e-d/index.html">NO_TOWED_CARAVAN_ALLOWED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1499613554%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o_-t-o-w-e-d_-c-a-r-a-v-a-n_-a-l-l-o-w-e-d/index.html">NO_TOWED_CARAVAN_ALLOWED</a></div></div><div class="brief "><p class="paragraph">A sign indicating no towed caravan allowed. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_Kingdom#/media/File:UK_traffic_sign_622.7.svg">No towed caravan allowed sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1429612561%2FClasslikes%2F1617540583" anchor-label="NO_TOWED_TRAILER_ALLOWED" id="-1429612561%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o_-t-o-w-e-d_-t-r-a-i-l-e-r_-a-l-l-o-w-e-d/index.html">NO_TOWED_TRAILER_ALLOWED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1429612561%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o_-t-o-w-e-d_-t-r-a-i-l-e-r_-a-l-l-o-w-e-d/index.html">NO_TOWED_TRAILER_ALLOWED</a></div></div><div class="brief "><p class="paragraph">A sign indicating no towed trailer allowed. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Sweden#/media/File:Sweden_road_sign_C6.svg">No towed trailer allowed sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1326368649%2FClasslikes%2F1617540583" anchor-label="NO_CAMPER_OR_MOTORHOME_ALLOWED" id="1326368649%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o_-c-a-m-p-e-r_-o-r_-m-o-t-o-r-h-o-m-e_-a-l-l-o-w-e-d/index.html">NO_CAMPER_OR_MOTORHOME_ALLOWED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1326368649%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o_-c-a-m-p-e-r_-o-r_-m-o-t-o-r-h-o-m-e_-a-l-l-o-w-e-d/index.html">NO_CAMPER_OR_MOTORHOME_ALLOWED</a></div></div><div class="brief "><p class="paragraph">A sign indicating no camper or motorhome allowed. Example: No examples available.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1362763146%2FClasslikes%2F1617540583" anchor-label="NO_TURN_ON_RED" id="1362763146%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-n-o_-t-u-r-n_-o-n_-r-e-d/index.html">NO_TURN_ON_RED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1362763146%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-n-o_-t-u-r-n_-o-n_-r-e-d/index.html">NO_TURN_ON_RED</a></div></div><div class="brief "><p class="paragraph">A sign indicating no turning on red permitted. Example: <a href="https://en.wikipedia.org/wiki/Turn_on_red#/media/File:CA-QC_road_sign_P-115-1.svg">No turn on red sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-600345971%2FClasslikes%2F1617540583" anchor-label="TURN_PERMITTED_ON_RED" id="-600345971%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-u-r-n_-p-e-r-m-i-t-t-e-d_-o-n_-r-e-d/index.html">TURN_PERMITTED_ON_RED</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-600345971%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-u-r-n_-p-e-r-m-i-t-t-e-d_-o-n_-r-e-d/index.html">TURN_PERMITTED_ON_RED</a></div></div><div class="brief "><p class="paragraph">A sign indicating turning on red permitted. Example: <a href="https://en.wikipedia.org/wiki/Turn_on_red#/media/File:Chile_road_sign_RA-2.svg">Turn permitted on red sign</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1360511280%2FClasslikes%2F1617540583" anchor-label="TWO_STAGE_LEFT" id="1360511280%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-w-o_-s-t-a-g-e_-l-e-f-t/index.html">TWO_STAGE_LEFT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1360511280%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-w-o_-s-t-a-g-e_-l-e-f-t/index.html">TWO_STAGE_LEFT</a></div></div><div class="brief "><p class="paragraph">A sign indicating that turning left requires a two-stage maneuver, also known as a hook turn or Copenhagen Left, which is a special maneuver to safely make a left turn at an intersection without crossing oncoming traffic. This maneuver applies only in right-hand driving countries and is particularly beneficial for cyclists, as it minimizes interaction with oncoming traffic, allowing for safer crossings. Example: <a href="https://medium.com/@maharudrabhishekkumar/understanding-two-stage-turns-for-cyclists-safer-crossings-made-simple-navigating-busy-e028f07bcc79">Two stage left turn</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="270667611%2FClasslikes%2F1617540583" anchor-label="TWO_STAGE_RIGHT" id="270667611%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="ENTRY" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-t-w-o_-s-t-a-g-e_-r-i-g-h-t/index.html">TWO_STAGE_RIGHT</a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="270667611%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><a href="-t-w-o_-s-t-a-g-e_-r-i-g-h-t/index.html">TWO_STAGE_RIGHT</a></div></div><div class="brief "><p class="paragraph">A sign indicating turning right with the specified vehicle type requires a two stage maneuver. A TWO_STAGE_RIGHT maneuver, is a special maneuver commonly used by cyclists to safely make a right turn at an intersection without crossing oncoming traffic. This maneuver is applicable only in left-hand driving countries and is particularly beneficial for cyclists as they allow for safer crossings by minimizing the interaction with oncoming traffic. Example: <a href="https://medium.com/@maharudrabhishekkumar/understanding-two-stage-turns-for-cyclists-safer-crossings-made-simple-navigating-busy-e028f07bcc79">Two stage right turn</a></p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="439923919%2FProperties%2F1617540583" anchor-label="entries" id="439923919%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="entries.html"><span><span>entries</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="439923919%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="entries.html">entries</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a><span class="token operator">&lt;</span><a href="index.html">RoadSignType</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1136310158%2FProperties%2F1617540583" anchor-label="value" id="1136310158%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value.html"><span><span>value</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1136310158%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block"><span class="token annotation builtin">@</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html"><span class="token annotation builtin">JvmField</span></a></div></div><span class="token keyword">val </span><a href="value.html">value</a><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-760368851%2FFunctions%2F1617540583" anchor-label="valueOf" id="-760368851%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="value-of.html"><span>value</span><wbr></wbr><span><span>Of</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-760368851%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="value-of.html"><span class="token function">valueOf</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">value<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="index.html">RoadSignType</a></div><div class="brief "><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1862835975%2FFunctions%2F1617540583" anchor-label="values" id="-1862835975%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="values.html"><span><span>values</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1862835975%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><a href="values.html"><span class="token function">values</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a><span class="token operator">&lt;</span><a href="index.html">RoadSignType</a><span class="token operator">&gt;</span></div><div class="brief "><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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

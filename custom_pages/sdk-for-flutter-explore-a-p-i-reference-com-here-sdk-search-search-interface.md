---
title: "SearchInterface"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-search-search-interface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>SearchInterface</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.search/SearchInterface///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.search</a><span class="delimiter">/</span><span class="current">SearchInterface</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Search</span><wbr></wbr><span><span>Interface</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">interface </span><a href="index.html">SearchInterface</a></div><p class="paragraph">Provides the interface for the online and offline search engines.</p><h4 class="">Inheritors</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="../-search-engine/index.html">SearchEngine</a></div></span></div><div></div></div></div></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-859402960%2FFunctions%2F1617540583" anchor-label="searchByAddress" id="-859402960%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-address.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span><span>Address</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-859402960%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="search-by-address.html"><span class="token function">searchByAddress</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-address-query/index.html">AddressQuery</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-search-callback/index.html">SearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous address query search for <a href="../-place/index.html">com.here.sdk.search.Place</a> instances. This is the same type of search as forward geocoding, except that more data is returned than just the geographic coordinates of a given address. Note that an address can belong to more than one <a href="../-place/index.html">com.here.sdk.search.Place</a> result, although all found places will share the same geographic coordinates. The returned places are sorted by relevance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1565320426%2FFunctions%2F1617540583" anchor-label="searchByCategory" id="1565320426%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-category.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span><span>Category</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1565320426%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="search-by-category.html"><span class="token function">searchByCategory</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-category-query/index.html">CategoryQuery</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-search-callback/index.html">SearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous category search for <a href="../-place/index.html">com.here.sdk.search.Place</a> instances. A list containing at least one <a href="../-place-category/index.html">com.here.sdk.search.PlaceCategory</a> must be provided as part of the com.here.sdk.search.SearchInterface.searchByCategory.query.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="159331414%2FFunctions%2F1617540583" anchor-label="searchByCoordinates" id="159331414%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-coordinates.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span><span>Coordinates</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="159331414%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="search-by-coordinates.html"><span class="token function">searchByCoordinates</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">coordinates<span class="token operator">: </span><a href="../../com.here.sdk.core/-geo-coordinates/index.html">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-search-callback/index.html">SearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous search for <a href="../-place/index.html">com.here.sdk.search.Place</a> instances based on the given geographic coordinates. This is the same search type as reverse geocoding, except that more data is returned than just the <a href="../-address/index.html">com.here.sdk.search.Address</a> related to the given coordinates. Note that more than one <a href="../-place/index.html">com.here.sdk.search.Place</a> can be related to the given coordinates. The returned places are sorted by relevance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-415195880%2FFunctions%2F1617540583" anchor-label="searchByPickedPlace" id="-415195880%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-picked-place.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span>Picked</span><wbr></wbr><span><span>Place</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-415195880%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="search-by-picked-place.html"><span class="token function">searchByPickedPlace</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">pickedPlace<span class="token operator">: </span><a href="../../com.here.sdk.core/-picked-place/index.html">PickedPlace</a><span class="token punctuation">, </span></span><span class="parameter ">languageCode<span class="token operator">: </span><a href="../../com.here.sdk.core/-language-code/index.html">LanguageCode</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-place-id-search-callback/index.html">PlaceIdSearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous search for a <a href="../-place/index.html">com.here.sdk.search.Place</a> based on the content found in <a href="../../com.here.sdk.core/-picked-place/index.html">com.here.sdk.core.PickedPlace</a>. If <a href="../../com.here.sdk.core/-picked-place/index.html">com.here.sdk.core.PickedPlace</a> data is obtained from the offline map, it may happen that the newer version that is used by the online service represented by <code class="lang-kotlin">SearchEngine</code> no longer contains the related POI. In that case, <a href="../-search-error/-n-o_-r-e-s-u-l-t-s_-f-o-u-n-d/index.html">com.here.sdk.search.SearchError.NO_RESULTS_FOUND</a> error is reported. When that happens, you may try to obtain the POI from the offline map by calling <code class="lang-kotlin">OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-729501317%2FFunctions%2F1617540583" anchor-label="searchByPlaceId" id="-729501317%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-place-id.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span>Place</span><wbr></wbr><span><span>Id</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-729501317%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="search-by-place-id.html"><span class="token function">searchByPlaceId</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-place-id-query/index.html">PlaceIdQuery</a><span class="token punctuation">, </span></span><span class="parameter ">languageCode<span class="token operator">: </span><a href="../../com.here.sdk.core/-language-code/index.html">LanguageCode</a><span class="token operator">?</span><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-place-id-search-callback/index.html">PlaceIdSearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous search for a <a href="../-place/index.html">com.here.sdk.search.Place</a> based on its ID and <a href="../../com.here.sdk.core/-language-code/index.html">com.here.sdk.core.LanguageCode</a>.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="972397708%2FFunctions%2F1617540583" anchor-label="searchByText" id="972397708%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="search-by-text.html"><span>search</span><wbr></wbr><span>By</span><wbr></wbr><span><span>Text</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="972397708%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="search-by-text.html"><span class="token function">searchByText</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-text-query/index.html">TextQuery</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-search-callback/index.html">SearchCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous text query search for <a href="../-place/index.html">com.here.sdk.search.Place</a> instances within a given <a href="../-text-query/-area/index.html">com.here.sdk.search.TextQuery.Area</a>. The returned places are sorted by relevance.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1109038724%2FFunctions%2F1617540583" anchor-label="suggestByText" id="-1109038724%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="suggest-by-text.html"><span>suggest</span><wbr></wbr><span>By</span><wbr></wbr><span><span>Text</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1109038724%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">abstract </span><span class="token keyword">fun </span><a href="suggest-by-text.html"><span class="token function">suggestByText</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">query<span class="token operator">: </span><a href="../-text-query/index.html">TextQuery</a><span class="token punctuation">, </span></span><span class="parameter ">options<span class="token operator">: </span><a href="../-search-options/index.html">SearchOptions</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="../-suggest-callback/index.html">SuggestCallback</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../../com.here.sdk.core.threading/-task-handle/index.html">TaskHandle</a></div><div class="brief "><p class="paragraph">Performs an asynchronous request to suggest places for text queries and returns suggestions sorted by relevance.</p></div></div></div>
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

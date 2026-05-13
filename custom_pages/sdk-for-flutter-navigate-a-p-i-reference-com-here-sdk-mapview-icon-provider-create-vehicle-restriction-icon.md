---
title: "createVehicleRestrictionIcon"
slug: "sdk-for-flutter-navigate-a-p-i-reference-com-here-sdk-mapview-icon-provider-create-vehicle-restriction-icon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- create-vehicle-restriction-icon.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>createVehicleRestrictionIcon</title>
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
<div class="main-content" data-page-type="member" id="content" pageIds="API Reference::com.here.sdk.mapview/IconProvider/createVehicleRestrictionIcon/#com.here.sdk.mapview.PickMapContentResult.VehicleRestrictionResult#com.here.sdk.mapview.MapScheme#com.here.sdk.mapview.IconProviderAssetType#com.here.sdk.core.Size2D#com.here.sdk.mapview.IconProvider.IconCallback/PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><a href="index.html">IconProvider</a><span class="delimiter">/</span><span class="current">createVehicleRestrictionIcon</span></div>
  <div class="cover ">
    <h1 class="cover"><span>create</span><wbr></wbr><span>Vehicle</span><wbr></wbr><span>Restriction</span><wbr></wbr><span><span>Icon</span></span></h1>
  </div>
  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="create-vehicle-restriction-icon.html"><span class="token function">createVehicleRestrictionIcon</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>pickingResult<span class="token operator">: </span><a href="../-pick-map-content-result/-vehicle-restriction-result/index.html">PickMapContentResult.VehicleRestrictionResult</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>mapScheme<span class="token operator">: </span><a href="../-map-scheme/index.html">MapScheme</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>assetType<span class="token operator">: </span><a href="../-icon-provider-asset-type/index.html">IconProviderAssetType</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>sizeConstraintsInPixels<span class="token operator">: </span><a href="../../com.here.sdk.core/-size2-d/index.html">Size2D</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>callback<span class="token operator">: </span><a href="-icon-callback/index.html">IconProvider.IconCallback</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates an image representing a vehicle restriction as shown on the map, based on map content picking result.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>picking</span><wbr></wbr><span><span>Result</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The result of picking vehicle restrictions.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>map</span><wbr></wbr><span><span>Scheme</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The map scheme for which the vehicle restriction icon should be created.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>asset</span><wbr></wbr><span><span>Type</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The asset type for which the vehicle restriction icon should be created.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>size</span><wbr></wbr><span>Constraints</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Pixels</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The maximum width and height of the icon in pixels. The values are capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If either width or height is set to 0, it will be calculated automatically based on icon's aspect ratio.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The callback which is used to return the created image, or an error code.</p></div></div></div></div></div><hr><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">fun </span><a href="create-vehicle-restriction-icon.html"><span class="token function">createVehicleRestrictionIcon</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>iconProperties<span class="token operator">: </span><a href="../-vehicle-restriction-icon-properties/index.html">VehicleRestrictionIconProperties</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>mapScheme<span class="token operator">: </span><a href="../-map-scheme/index.html">MapScheme</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>assetType<span class="token operator">: </span><a href="../-icon-provider-asset-type/index.html">IconProviderAssetType</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>sizeConstraintsInPixels<span class="token operator">: </span><a href="../../com.here.sdk.core/-size2-d/index.html">Size2D</a><span class="token punctuation">, </span></span><span class="parameter "><span><span class="token annotation builtin">@</span><a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html"><span class="token annotation builtin">NonNull</span></a> </span>callback<span class="token operator">: </span><a href="-icon-callback/index.html">IconProvider.IconCallback</a></span></span><span class="token punctuation">)</span></div><p class="paragraph">Creates an image representing a vehicle restriction as shown on the map. </p><p class="paragraph"> In case when `VehicleRestriction` object specifies multiple types of restrictions, then the icon is generated for the first one according to the following priority: <a href="../../com.here.sdk.transport/-vehicle-restriction/restriction.html">restriction</a>, <a href="../../com.here.sdk.transport/-vehicle-restriction/axle-count.html">axleCount</a>, <a href="../../com.here.sdk.transport/-vehicle-restriction/axle-count-in-group.html">axleCountInGroup</a>, <a href="../../com.here.sdk.transport/-vehicle-restriction/hazmat-restriction.html">hazmatRestriction</a>, <a href="../../com.here.sdk.transport/-vehicle-restriction/trailer-count.html">trailerCount</a>.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>icon</span><wbr></wbr><span><span>Properties</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The properties of the icon.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>map</span><wbr></wbr><span><span>Scheme</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The map scheme for which the vehicle restriction icon should be created.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>asset</span><wbr></wbr><span><span>Type</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The asset type for which the vehicle restriction icon should be created.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span>size</span><wbr></wbr><span>Constraints</span><wbr></wbr><span>In</span><wbr></wbr><span><span>Pixels</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The maximum width and height of the icon in pixels. The values are capped to a maximum of 4096 pixels. The image will be created as large as possible within the width and height constraints while maintaining the aspect ratio. If either width or height is set to 0, it will be calculated automatically based on icon's aspect ratio.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><u><span><span>callback</span></span></u></div></span></div><div><div class="title"><p class="paragraph">The callback which is used to return the created image, or an error code.</p></div></div></div></div></div></div></div>
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

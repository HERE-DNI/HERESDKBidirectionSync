---
title: "MeshBuilder"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-mesh-builder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MeshBuilder</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MeshBuilder///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="../../../index.html">API Reference</a><span class="delimiter">/</span><a href="../index.html">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MeshBuilder</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Mesh</span><wbr></wbr><span><span>Builder</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">open </span><span class="token keyword">class </span><a href="index.html">MeshBuilder</a> : <a href="../../com.here/-native-base/index.html">NativeBase</a></div><p class="paragraph">Builder for meshes. Such meshes can contain different kinds of primitives, like quads or triangles. Both primitives support adding texture coordinates that are mapped to the corners of the primitives. See <a href="../-triangle-mesh-builder/index.html">com.here.sdk.mapview.TriangleMeshBuilder</a> and <a href="../-quad-mesh-builder/index.html">com.here.sdk.mapview.QuadMeshBuilder</a> for more details.</p><p class="paragraph">Note: Normals cannot be set as they are not necessary when using the <a href="index.html">com.here.sdk.mapview.MeshBuilder</a>.</p><p class="paragraph"><strong>Example how to build a cube using </strong><a href="../-quad-mesh-builder/index.html"><strong>com.here.sdk.mapview.QuadMeshBuilder</strong></a></p><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">Mesh cube = new MeshBuilder()<br>    .quad(new Point3D(0.5, 0.5, 0.5),<br>        new Point3D(-0.5, 0.5, 0.5),<br>        new Point3D(0.5, -0.5, 0.5),<br>        new Point3D(-0.5, -0.5, 0.5))<br>    .quad(new Point3D(-0.5, 0.5, -0.5),<br>        new Point3D(0.5, 0.5, -0.5),<br>        new Point3D(-0.5, -0.5, -0.5),<br>        new Point3D(0.5, -0.5, -0.5))<br>    .quad(new Point3D(0.5, 0.5, -0.5),<br>        new Point3D(0.5, 0.5, 0.5),<br>        new Point3D(0.5, -0.5, -0.5),<br>        new Point3D(0.5, -0.5, 0.5))<br>    .quad(new Point3D(-0.5, 0.5, 0.5),<br>        new Point3D(-0.5, 0.5, -0.5),<br>        new Point3D(-0.5, -0.5, 0.5),<br>        new Point3D(-0.5, -0.5, -0.5))<br>    .quad(new Point3D(-0.5, 0.5, 0.5),<br>        new Point3D(0.5, 0.5, 0.5),<br>        new Point3D(-0.5, 0.5, -0.5),<br>        new Point3D(0.5, 0.5, -0.5))<br>    .quad(new Point3D(0.5, -0.5, 0.5),<br>        new Point3D(-0.5, -0.5, 0.5),<br>        new Point3D(0.5, -0.5, -0.5),<br>        new Point3D(-0.5, -0.5, -0.5))<br>    .build();</code></pre><span class="top-right-position"><span class="copy-icon"></span><div class="copy-popup-wrapper popup-to-left"><span class="copy-popup-icon"></span><span>Content copied to clipboard</span></div></span></div><h4 class="">Inheritors</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="../-quad-mesh-builder/index.html">QuadMeshBuilder</a></div></span></div><div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue "><div class=""><span class="inline-flex"><div><a href="../-triangle-mesh-builder/index.html">TriangleMeshBuilder</a></div></span></div><div></div></div></div></div></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="CONSTRUCTOR">
        <h2 class="">Constructors</h2>
        <div class="table"><a data-name="-450595613%2FConstructors%2F1617540583" anchor-label="MeshBuilder" id="-450595613%2FConstructors%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-togglable="CONSTRUCTOR" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-mesh-builder.html"><span>Mesh</span><wbr></wbr><span><span>Builder</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-450595613%2FConstructors%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">constructor</span><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Constructs an instance of MeshBuilder.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="1363862584%2FClasslikes%2F1617540583" anchor-label="Companion" id="1363862584%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="-companion/index.html"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1363862584%2FClasslikes%2F1617540583"></span>
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
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="-274825661%2FFunctions%2F1617540583" anchor-label="build" id="-274825661%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="build.html"><span><span>build</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-274825661%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="build.html"><span class="token function">build</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-mesh/index.html">Mesh</a><span class="token operator">?</span></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1268032301%2FFunctions%2F1617540583" anchor-label="quad" id="1268032301%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="quad.html"><span><span>quad</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1268032301%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="quad.html"><span class="token function">quad</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">a<span class="token operator">: </span><a href="../../com.here.sdk.core/-point3-d/index.html">Point3D</a><span class="token punctuation">, </span></span><span class="parameter ">b<span class="token operator">: </span><a href="../../com.here.sdk.core/-point3-d/index.html">Point3D</a><span class="token punctuation">, </span></span><span class="parameter ">c<span class="token operator">: </span><a href="../../com.here.sdk.core/-point3-d/index.html">Point3D</a><span class="token punctuation">, </span></span><span class="parameter ">d<span class="token operator">: </span><a href="../../com.here.sdk.core/-point3-d/index.html">Point3D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-quad-mesh-builder/index.html">QuadMeshBuilder</a></div><div class="brief "><p class="paragraph">Adds a quad. Internally, this will be transformed into triangles abc and bdc.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-843619262%2FFunctions%2F1617540583" anchor-label="triangle" id="-843619262%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="triangle.html"><span><span>triangle</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-843619262%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="triangle.html"><span class="token function">triangle</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">a<span class="token operator">: </span><a href="../../com.here.sdk.core/-point3-d/index.html">Point3D</a><span class="token punctuation">, </span></span><span class="parameter ">b<span class="token operator">: </span><a href="../../com.here.sdk.core/-point3-d/index.html">Point3D</a><span class="token punctuation">, </span></span><span class="parameter ">c<span class="token operator">: </span><a href="../../com.here.sdk.core/-point3-d/index.html">Point3D</a></span></span><span class="token punctuation">)</span><span class="token operator">: </span><a href="../-triangle-mesh-builder/index.html">TriangleMeshBuilder</a></div><div class="brief "><p class="paragraph">Adds a triangle.</p></div></div></div>
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

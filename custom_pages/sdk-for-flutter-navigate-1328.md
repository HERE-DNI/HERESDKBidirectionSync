---
title: "MapCamera"
slug: "sdk-for-flutter-navigate"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- index.html -->
<!DOCTYPE html>
<html class="no-js">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <title>MapCamera</title>
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
<div class="main-content" data-page-type="classlike" id="content" pageIds="API Reference::com.here.sdk.mapview/MapCamera///PointingToDeclaration//1617540583">
  <div class="breadcrumbs"><a href="sdk-for-flutter-explore-index">API Reference</a><span class="delimiter">/</span><a href="sdk-for-flutter-explore-index">com.here.sdk.mapview</a><span class="delimiter">/</span><span class="current">MapCamera</span></div>
  <div class="cover ">
    <h1 class="cover"><span>Map</span><wbr></wbr><span><span>Camera</span></span></h1>
    <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">MapCamera</a> : <a href="sdk-for-flutter-explore-index">NativeBase</a></div><p class="paragraph">Represents the camera looking onto the map view.</p><p class="paragraph">Each map instance has exactly one camera that is used to manipulate the way the map is displayed.</p><p class="paragraph">Any updates to the state of the camera will be applied while drawing the next map view frame and the current state of the camera reflects what is currently drawn inside the map view.</p><p class="paragraph">Note: The camera can be configured and positioned even before a map scene is loaded for the first time. This allows for pre-setting the desired camera position, orientation, and zoom level, which will be applied once the map scene becomes available.</p><p class="paragraph"><b>Camera Model</b></p><p class="paragraph"><i>Camera Concepts and Units</i></p><p class="paragraph">By default, HERE SDK uses an idealized Earth globe with a 3D-capable camera model. Being a 3D camera model means that the world position can be freely specified in geodetic 3D space (i.e. Earth centric) and the orientation can be freely changed around two axes - bearing (also known as head) and tilt (also known as pitch).</p><p class="paragraph">The camera supports the look-at target with orientation on the ground way of setting up the camera in space. The camera is placed so that it looks at a specific geo-coordinates (placed at the <code class="lang-kotlin">principal point</code>) from a given orientation and distance.</p><ul><li><p class="paragraph">the look-at target in geo-coordinates (latitude, longitude) in degrees and an <code class="lang-kotlin">altitude</code> in meters above MSL (mean sea level) at the <code class="lang-kotlin">principal point</code></p></li><li><p class="paragraph">the <code class="lang-kotlin">orientation</code> at the look-at target</p></li><li><p class="paragraph">the distance of the camera from the look-at target, given as <code class="lang-kotlin">distance</code> in meters or as <code class="lang-kotlin">zoom-level</code></p></li></ul><p class="paragraph"><i>Getting the current camera state</i></p><p class="paragraph">The current camera state can be obtained by the <a href="sdk-for-flutter-explore-state">com.here.sdk.mapview.MapCamera.state</a> call. It contains information about the camera look-at target (geo-coordinates and orientation) in geodetic space. The values are returned for the current <code class="lang-kotlin">principal point</code>. This can lead to surprising or unexpected values in cases where the camera position/orientation was specified for another screen point, e.g. when using <a href="sdk-for-flutter-explore-look-at">com.here.sdk.mapview.MapCameraUpdateFactory.lookAt</a> with a view rectangle, whose center does not coincide with the <code class="lang-kotlin">principal point</code>.  In this case, the geo-coordinates of the look-at target will differ from the center of the geo-box used in the <code class="lang-kotlin">lookAt</code> call.</p><p class="paragraph"><i>Geo coordinates</i></p><p class="paragraph">Geo-coordinates are given in degrees and follow the common nomenclature of positive northern latitudes and positive eastern longitudes.</p><p class="paragraph"><i>Altitude</i></p><p class="paragraph">When <code class="lang-kotlin">altitude</code> is specified, it is always in meters above mean sea level (MSL). If this value is invalid (not-a-number) or not specified, then the terrain height at the given geo-coordinates will be looked up from the map. This is especially interesting in cases where terrain elevation is used within the map display.</p><p class="paragraph"><i>Distance vs zoom-level vs scale</i></p><p class="paragraph">Map camera <code class="lang-kotlin">distance</code>, <code class="lang-kotlin">zoom-level</code> and <code class="lang-kotlin">scale</code> determine how much of the world is visible on the HERE map. <code class="lang-kotlin">Distance</code>, <code class="lang-kotlin">zoom-level</code> and <code class="lang-kotlin">scale</code> are directly connected and changing one will automatically change the others as well (except for <code class="lang-kotlin">distance</code>/<code class="lang-kotlin">scale</code> changes that map to <code class="lang-kotlin">zoom-level</code> values < 0 or 23).</p><ul><li><p class="paragraph"><code class="lang-kotlin">distance</code>: the distance from the camera to the look-at target on the surface of the Earth, in meters</p></li><li><p class="paragraph"><code class="lang-kotlin">zoom-level</code>: the map zoom level, in the range \[0, 3]. The relation between the width of the equator in logical pixels <code class="lang-kotlin">w</code> and the zoom level <code class="lang-kotlin">z</code> is: <code class="lang-kotlin">w = 256 * 2^(z)</code></p></li><li><p class="paragraph"><code class="lang-kotlin">scale</code>: the scale of the map at the look-at target in meters on screen per meters on Earth. So a scale of 0.001 shows 10 meters on Earth within 1 cm on screen.</p></li></ul><p class="paragraph">The following mapping represents the <code class="lang-kotlin">zoom-level</code> values:</p><table><thead><tr><th>zoom-level</th><th>~ scale on screen (130dpi)</th><th>width of the equator in logical pixels</th><th>what can be seen</th></tr></thead><tbody><tr><td>0</td><td>1:800 million</td><td>256</td><td>Earth</td></tr><tr><td>1</td><td>1:400 million</td><td>512</td><td></td></tr><tr><td>2</td><td>1:200 million</td><td>1024</td><td></td></tr><tr><td>3</td><td>1:100 million</td><td>2048</td><td></td></tr><tr><td>4</td><td>1:50 million</td><td>4096</td><td>A continent</td></tr><tr><td>5</td><td>1:25 million</td><td>8192</td><td>Large roads</td></tr><tr><td>6</td><td>1:12 million</td><td>16384</td><td>Large rivers</td></tr><tr><td>7</td><td>1:6 million</td><td>32768</td><td>A country</td></tr><tr><td>8</td><td>1:3 million</td><td>65536</td><td></td></tr><tr><td>9</td><td>1:1 million</td><td>131072</td><td></td></tr><tr><td>10</td><td>1:780 thousand</td><td>262144</td><td></td></tr><tr><td>11</td><td>1:390 thousand</td><td>524288</td><td></td></tr><tr><td>12</td><td>1:195 thousand</td><td>1048576</td><td></td></tr><tr><td>13</td><td>1:100 thousand</td><td>2097152</td><td></td></tr><tr><td>14</td><td>1:50 thousand</td><td>4194304</td><td>A city</td></tr><tr><td>15</td><td>1:25 thousand</td><td>8388608</td><td></td></tr><tr><td>16</td><td>1:12 thousand</td><td>16777216</td><td>Buildings</td></tr><tr><td>17</td><td>1:6 thousand</td><td>33554432</td><td>Landmarks</td></tr><tr><td>18</td><td>1:3 thousand</td><td>67108864</td><td></td></tr><tr><td>19</td><td>1:1 thousand</td><td>134217728</td><td></td></tr><tr><td>20</td><td>1:7 hundred</td><td>268435456</td><td>Streets</td></tr><tr><td>21</td><td>1:3 hundred</td><td>536870912</td><td></td></tr><tr><td>22</td><td>1:1 hundred</td><td>1073741824</td><td></td></tr><tr><td>23</td><td>1:95</td><td>2147483648</td><td></td></tr></tbody></table><p class="paragraph"><i>Orientation</i></p><p class="paragraph">The camera <code class="lang-kotlin">orientation</code> is composed of two parts:</p><ul><li><p class="paragraph"><code class="lang-kotlin">bearing</code>: also known as azimuth, the view direction in clockwise degrees; 0° = north, 90° = east, 180° = south, 270° = west</p></li><li><p class="paragraph"><code class="lang-kotlin">tilt</code>: the angle in degrees from the vertical that the camera is looking down at the Earth; 0° = straight down.</p></li></ul><p class="paragraph"><i>Changing the Camera</i></p><p class="paragraph">All changes to the camera are encapsulated in camera updates that are created using the methods in the <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapCameraUpdateFactory</a> class.</p><p class="paragraph">These updates can then be applied to the <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.HereMap</a> using <a href="sdk-for-flutter-explore-apply-update">com.here.sdk.mapview.MapCamera.applyUpdate</a>.</p><p class="paragraph">Camera updates are queued and executed when the next frame is rendered. They are executed in the order in which they were applied.</p><p class="paragraph"><i>Animating the Camera</i></p><p class="paragraph">Camera updates can be animated by first creating a camera animation using the methods in the <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.MapCameraAnimationFactory</a> class and then applying this animation to the <a href="sdk-for-flutter-explore-index">com.here.sdk.mapview.HereMap</a> using <a href="sdk-for-flutter-explore-start-animation">com.here.sdk.mapview.MapCamera.startAnimation</a>.</p><p class="paragraph">Only one camera animation for one camera component at a time is supported. Applying a new animation will cancel the active animation before the new one is started. The start position in this case is where ever the active animation happened to be at the time. Different components are camera state (<code class="lang-kotlin">target pose</code> and <code class="lang-kotlin">distance/zoom level/scale</code>) and camera projection (<code class="lang-kotlin">field of view</code>, <code class="lang-kotlin">focal length</code> and <code class="lang-kotlin">principal point</code>).</p><p class="paragraph">The running animations can also be canceled using <a href="sdk-for-flutter-explore-cancel-animations">com.here.sdk.mapview.MapCamera.cancelAnimations</a> or individual ones using <a href="sdk-for-flutter-explore-cancel-animation">com.here.sdk.mapview.MapCamera.cancelAnimation</a>.</p></div></div>
  </div>
  <div class="tabbedcontent">
    <div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
    <div class="tabs-section-body">
      <div data-togglable="TYPE">
        <h2 class="">Types</h2>
        <div class="table"><a data-name="-2140172955%2FClasslikes%2F1617540583" anchor-label="Companion" id="-2140172955%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>Companion</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2140172955%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">object </span><a href="sdk-for-flutter-explore-index">Companion</a></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1403522995%2FClasslikes%2F1617540583" anchor-label="DryCameraUpdateCallback" id="1403522995%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Dry</span><wbr></wbr><span>Camera</span><wbr></wbr><span>Update</span><wbr></wbr><span><span>Callback</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1403522995%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">fun </span><span class="token keyword">interface </span><a href="sdk-for-flutter-explore-index">DryCameraUpdateCallback</a></div><div class="brief "><p class="paragraph">Used to report back results of dry update application to camera.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="530304160%2FClasslikes%2F1617540583" anchor-label="FarPlaneConfiguration" id="530304160%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span>Far</span><wbr></wbr><span>Plane</span><wbr></wbr><span><span>Configuration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="530304160%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">FarPlaneConfiguration</a></div><div class="brief "><p class="paragraph">Far plane distance configuration for a zoom level.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1756472448%2FClasslikes%2F1617540583" anchor-label="State" id="-1756472448%2FClasslikes%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-index"><span><span>State</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1756472448%2FClasslikes%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">class </span><a href="sdk-for-flutter-explore-index">State</a></div><div class="brief "><p class="paragraph">Encapsulates state of the camera.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="PROPERTY">
        <h2 class="">Properties</h2>
        <div class="table"><a data-name="1971793975%2FProperties%2F1617540583" anchor-label="boundingBox" id="1971793975%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-bounding-box"><span>bounding</span><wbr></wbr><span><span>Box</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1971793975%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-bounding-box">boundingBox</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoBox</a><span class="token operator">?</span></div><div class="brief "><p class="paragraph">Currently visible map area encompassed in a GeoBox. Note that this bounding box is always rectangular, and its sides are always parallel to the latitude and longitude. If the camera is rotated, the returned bounding box will be a circumscribed rectangle that is larger than the visible map area. Similarly, when the map is tilted (for example, if the map is tilted by 45 degrees), the visible map area represents a trapezoidal area in the world. Resulting value will then be a larger circumscribed rectangle that contains this trapezoid area. Because on this, corners of the resulting bounding box may be located outside of the currently visible area.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-73896476%2FProperties%2F1617540583" anchor-label="limits" id="-73896476%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-limits"><span><span>limits</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-73896476%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-limits">limits</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraLimits</a></div><div class="brief "><p class="paragraph">Controls limits for the camera settings.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-133913542%2FProperties%2F1617540583" anchor-label="principalPoint" id="-133913542%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-principal-point"><span>principal</span><wbr></wbr><span><span>Point</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-133913542%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">var </span><a href="sdk-for-flutter-explore-principal-point">principalPoint</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></div><div class="brief "><p class="paragraph">Determines the pixel point where the target is placed within the map view. Setting a new principal point instantly moves the map to render the current target coordinates at the new principal point.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-239475411%2FProperties%2F1617540583" anchor-label="state" id="-239475411%2FProperties%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-state"><span><span>state</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-239475411%2FProperties%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">val </span><a href="sdk-for-flutter-explore-state">state</a><span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCamera.State</a></div><div class="brief "><p class="paragraph">Current state of the camera that reflects what is currently drawn by the map view.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div data-togglable="FUNCTION">
        <h2 class="">Functions</h2>
        <div class="table"><a data-name="919659942%2FFunctions%2F1617540583" anchor-label="addListener" id="919659942%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-add-listener"><span>add</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="919659942%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-add-listener"><span class="token function">addListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">listener<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Adds a listener to this camera that will be notified on the main thread every time the map is redrawn with new camera parameters.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1430173199%2FFunctions%2F1617540583" anchor-label="applyUpdate" id="1430173199%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-apply-update"><span>apply</span><wbr></wbr><span><span>Update</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1430173199%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-apply-update"><span class="token function">applyUpdate</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">cameraUpdate<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Applies camera update to the map camera.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1851544935%2FFunctions%2F1617540583" anchor-label="cancelAnimation" id="-1851544935%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-cancel-animation"><span>cancel</span><wbr></wbr><span><span>Animation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1851544935%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-cancel-animation"><span class="token function">cancelAnimation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">cameraAnimation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraAnimation</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Cancels an ongoing camera animation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="2020595923%2FFunctions%2F1617540583" anchor-label="cancelAnimations" id="2020595923%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-cancel-animations"><span>cancel</span><wbr></wbr><span><span>Animations</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="2020595923%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-cancel-animations"><span class="token function">cancelAnimations</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Cancels any ongoing camera animation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-2278392%2FFunctions%2F1617540583" anchor-label="dryApplyUpdate" id="-2278392%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-dry-apply-update"><span>dry</span><wbr></wbr><span>Apply</span><wbr></wbr><span><span>Update</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-2278392%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-dry-apply-update"><span class="token function">dryApplyUpdate</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">cameraUpdate<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">callback<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCamera.DryCameraUpdateCallback</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Computes result of applying camera update without changing state of the map camera.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1228059061%2FFunctions%2F1617540583" anchor-label="lookAt" id="1228059061%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-look-at"><span>look</span><wbr></wbr><span><span>At</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1228059061%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Makes the camera look at a new geodetic target, while preserving the current orientation and distance to the target.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoBox</a><span class="token punctuation">, </span></span><span class="parameter ">orientation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Makes the camera look at the specified geodetic area.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">zoom<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasure</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Makes the camera look at the geodetic target with the given zoom.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoBox</a><span class="token punctuation">, </span></span><span class="parameter ">orientation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">viewRectangle<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Rectangle2D</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Makes the camera look at the specified geodetic area and pass a rectangle which specifies where the area should appear inside of the map view.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-look-at"><span class="token function">lookAt</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">target<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoCoordinates</a><span class="token punctuation">, </span></span><span class="parameter ">orientation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">zoom<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapMeasure</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Makes the camera look at the geodetic target with the given zoom and orientation.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="200172438%2FFunctions%2F1617540583" anchor-label="orbitBy" id="200172438%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-orbit-by"><span>orbit</span><wbr></wbr><span><span>By</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="200172438%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-orbit-by"><span class="token function">orbitBy</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">delta<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a><span class="token punctuation">, </span></span><span class="parameter ">origin<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Orbits the camera around a specified view point by increasing tilt and bearing by specified delta values.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-83404287%2FFunctions%2F1617540583" anchor-label="removeListener" id="-83404287%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-listener"><span>remove</span><wbr></wbr><span><span>Listener</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-83404287%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-listener"><span class="token function">removeListener</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">observer<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes the listener from the camera.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1535403427%2FFunctions%2F1617540583" anchor-label="removeListeners" id="1535403427%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-remove-listeners"><span>remove</span><wbr></wbr><span><span>Listeners</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1535403427%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-remove-listeners"><span class="token function">removeListeners</span></a><span class="token punctuation">(</span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Removes all registered listeners.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1124118633%2FFunctions%2F1617540583" anchor-label="setDistanceToTarget" id="1124118633%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-distance-to-target"><span>set</span><wbr></wbr><span>Distance</span><wbr></wbr><span>To</span><wbr></wbr><span><span>Target</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1124118633%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-distance-to-target"><span class="token function">setDistanceToTarget</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">distanceInMeters<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Makes the camera look at current target from certain distance</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-849468779%2FFunctions%2F1617540583" anchor-label="setFarPlaneConfiguration" id="-849468779%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-far-plane-configuration"><span>set</span><wbr></wbr><span>Far</span><wbr></wbr><span>Plane</span><wbr></wbr><span><span>Configuration</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-849468779%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-far-plane-configuration"><span class="token function">setFarPlaneConfiguration</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">configs<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html">Map</a><span class="token operator">&lt;</span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span><a href="sdk-for-flutter-explore-index">MapCamera.FarPlaneConfiguration</a><span class="token operator">&gt;</span></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Sets far plane distance configs per zoom level.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="1354436760%2FFunctions%2F1617540583" anchor-label="setOrientationAtTarget" id="1354436760%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-set-orientation-at-target"><span>set</span><wbr></wbr><span>Orientation</span><wbr></wbr><span>At</span><wbr></wbr><span><span>Target</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="1354436760%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-set-orientation-at-target"><span class="token function">setOrientationAtTarget</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">orientation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">GeoOrientationUpdate</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Changes camera orientation in relation to target location.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1824565636%2FFunctions%2F1617540583" anchor-label="startAnimation" id="-1824565636%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-start-animation"><span>start</span><wbr></wbr><span><span>Animation</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1824565636%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-start-animation"><span class="token function">startAnimation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">cameraAnimation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraAnimation</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Starts a given camera animation.</p></div><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-start-animation"><span class="token function">startAnimation</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">cameraAnimation<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">MapCameraAnimation</a><span class="token punctuation">, </span></span><span class="parameter ">animationListener<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">AnimationListener</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Starts a given camera animation. The state of the animation can be tracked with the provided listener.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-624004995%2FFunctions%2F1617540583" anchor-label="zoomBy" id="-624004995%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-zoom-by"><span>zoom</span><wbr></wbr><span><span>By</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-624004995%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-zoom-by"><span class="token function">zoomBy</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">factor<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a><span class="token punctuation">, </span></span><span class="parameter ">origin<span class="token operator">: </span><a href="sdk-for-flutter-explore-index">Point2D</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Zooms in or out by a specified factor.</p></div></div></div>
                </div>
              </div>
            </div>
          </div>
<a data-name="-1950450954%2FFunctions%2F1617540583" anchor-label="zoomTo" id="-1950450954%2FFunctions%2F1617540583" data-filterable-set=":modules:dokkaHtml/release"></a>
          <div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
            <div class="main-subrow keyValue ">
              <div class=""><span class="inline-flex">
                  <div><a href="sdk-for-flutter-explore-zoom-to"><span>zoom</span><wbr></wbr><span><span>To</span></span></a></div>
<span class="anchor-wrapper"><span class="anchor-icon" pointing-to="-1950450954%2FFunctions%2F1617540583"></span>
                    <div class="copy-popup-wrapper "><span class="copy-popup-icon"></span><span>Link copied to clipboard</span></div>
                  </span></span></div>
              <div>
                <div class="title">
                  <div class="platform-hinted " data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><span class="token keyword">external </span><span class="token keyword">fun </span><a href="sdk-for-flutter-explore-zoom-to"><span class="token function">zoomTo</span></a><span class="token punctuation">(</span><span class="parameters "><span class="parameter ">zoomLevel<span class="token operator">: </span><a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></span></span><span class="token punctuation">)</span></div><div class="brief "><p class="paragraph">Zooms to the specified zoom level. The supplied value will be clamped to the range of \[0, 22\], where 0 is a view of whole globe and 22 is street level.</p></div></div></div>
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

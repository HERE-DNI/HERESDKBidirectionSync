---
title: "configureVehicleRestrictionFilter static method"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-configurevehiclerestrictionfilter"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- configureVehicleRestrictionFilter.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcontentsettings-class</li>
<li class="self-crumb">configureVehicleRestrictionFilter static method</li>
</ol>
<div class="self-name">configureVehicleRestrictionFilter</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview/MapContentSettings-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>configureVehicleRestrictionFilter static method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0, use [MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification] instead.")</li>
</ol>
</div>
void
configureVehicleRestrictionFilter(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-transport-transportmode transportMode, </li>
<li>/sdk-for-flutter-navigate-transport-truckspecifications-class truckSpecifications, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-transport-hazardousmaterial&gt;? hazardousMaterials, </li>
<li>/sdk-for-flutter-navigate-transport-tunnelcategory? tunnelCategory, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Configure a filter for /sdk-for-flutter-navigate-mapview-mapfeatures-vehiclerestrictions to show only the restrictions
matching the specified criteria when the feature is enabled.</p>
<h1 id="filtering-rules-for-truck-specifications">Filtering rules for truck specifications</h1>
<p>Only restrictions applicable to the supplied truck specifications will be shown.</p>
<p>Examples:</p>
<ul>
<li>If the height in <code>MapContentSettings.configureVehicleRestrictionFilter.truckSpecifications</code> is set to 200 cm, then height restrictions
with a height greater than 200 cm will not be displayed.</li>
<li>If the trailer count in <code>MapContentSettings.configureVehicleRestrictionFilter.truckSpecifications</code> is set to 2, then trailer
restrictions for a count greater than 2 will not be displayed.</li>
</ul>
<h1 id="filtering-rules-for-hazardous-materials">Filtering rules for hazardous materials</h1>
<p>Only restrictions applicable to specified hazardous materials will be shown.
If at least one hazardous material of any type is present in the list, all available
tunnel category restrictions will be displayed. In order to filter-out non-applicable
tunnel categories, a tunnel category, that applies to the vehicle, can be specified
additionally.</p>
<p>Examples:</p>
<ul>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials</code> contains /sdk-for-flutter-navigate-transport-hazardousmaterial
and /sdk-for-flutter-navigate-transport-hazardousmaterial, then only material restrictions
for poison and gas will be displayed.</li>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials</code> list is empty, then no material restrictions
will be shown.</li>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials</code> list is not supplied at all (is <code>null</code>), then
no material restrictions will be shown.</li>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials</code> contains at least one hazardous material of any
type and <code>MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory</code> is <code>null</code>, then only corresponding material
restrictions will be displayed together with all available tunnel categories.</li>
</ul>
<h1 id="filtering-rules-for-tunnel-category">Filtering rules for tunnel category</h1>
<p>Tunnel categories are labeled and rated based on the level of restriction they provide.
The lowest level of restriction is /sdk-for-flutter-navigate-transport-tunnelcategory, the highest and most
restrictive one is /sdk-for-flutter-navigate-transport-tunnelcategory.</p>
<p>Specifying tunnel category means that:</p>
<ul>
<li>The truck carries goods which could cause only the additional dangerous effects
described in specified tunnel category and other categories below it with lower level
of restriction.</li>
<li>The truck does not carry goods that could cause the dangerous effects described in
tunnel categories above with higher restriction levels than the one specified.</li>
</ul>
<p>Tunnel categories are closely related to hazardous materials.</p>
<p>Since the type of hazardous material alone does not define the exact level of danger,
to ensure comprehensive coverage; the HERE SDK follows:</p>
<ul>
<li>If at least one hazardous material is specified but no <code>MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory</code> is provided,
the SDK enables and displays <strong>all tunnel category restrictions</strong> to ensure that no relevant
restrictions are omitted.</li>
<li>If both hazardous materials and a <code>MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory</code> are specified, the SDK
<strong>strictly follows the given tunnel category parameter</strong> and displays only the
applicable restrictions.</li>
</ul>
<p>Example:
If <code>MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory</code> is set to /sdk-for-flutter-navigate-transport-tunnelcategory, then restrictions for
tunnel category /sdk-for-flutter-navigate-transport-tunnelcategory and /sdk-for-flutter-navigate-transport-tunnelcategory
will be displayed, but not the categories /sdk-for-flutter-navigate-transport-tunnelcategory and
/sdk-for-flutter-navigate-transport-tunnelcategory.</p>
<ul>
<li>
<p><code>transportMode</code> Specifies the current transport type. Currently, it's used to distinguish
between truck and other transport modes. This distinction ensures consistency
between the routing logic and the information displayed on the map.
At present, this is primarily used to suppress the generic truck restriction icon.</p>
</li>
<li>
<p><code>truckSpecifications</code> The size, weight, type and trailer count specifications to filter for, so that only
restrictions which are relevant for the given specifications are displayed.</p>
</li>
<li>
<p><code>hazardousMaterials</code> The hazardous materials to filter for, so that only applicable restrictions are
displayed. When the list is <code>null</code> or empty, then no material restrictions
will be displayed.</p>
</li>
<li>
<p><code>tunnelCategory</code> The tunnel category to filter for, so that only applicable restrictions are
displayed. If <code>null</code>, then no tunnel category restrictions will be
displayed.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0, use [MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification] instead.")

static void configureVehicleRestrictionFilter(TransportMode transportMode, TruckSpecifications truckSpecifications, List&lt;HazardousMaterial&gt;? hazardousMaterials, TunnelCategory? tunnelCategory) =&gt; $prototype.configureVehicleRestrictionFilter(transportMode, truckSpecifications, hazardousMaterials, tunnelCategory);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcontentsettings-class</li>
<li class="self-crumb">configureVehicleRestrictionFilter static method</li>
</ol>
<h5>MapContentSettings class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>

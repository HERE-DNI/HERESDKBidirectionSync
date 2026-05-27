---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-heremap-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- HereMap-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/HereMap-class.html#constructors">Constructors</a></li>
<li><a href="mapview/HereMap/HereMap.html">HereMap</a></li>
<li class="section-title">
<a href="mapview/HereMap-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/HereMap/gestureRecognizers.html">gestureRecognizers</a></li>
<li class="inherited"><a href="mapview/HereMap/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/HereMap/key.html">key</a></li>
<li><a href="mapview/HereMap/mode.html">mode</a></li>
<li><a href="mapview/HereMap/onMapCreated.html">onMapCreated</a></li>
<li class="inherited"><a href="mapview/HereMap/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/HereMap-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/HereMap/createElement.html">createElement</a></li>
<li><a href="mapview/HereMap/createState.html">createState</a></li>
<li class="inherited"><a href="mapview/HereMap/debugDescribeChildren.html">debugDescribeChildren</a></li>
<li class="inherited"><a href="mapview/HereMap/debugFillProperties.html">debugFillProperties</a></li>
<li class="inherited"><a href="mapview/HereMap/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/HereMap/toDiagnosticsNode.html">toDiagnosticsNode</a></li>
<li class="inherited"><a href="mapview/HereMap/toString.html">toString</a></li>
<li class="inherited"><a href="mapview/HereMap/toStringDeep.html">toStringDeep</a></li>
<li class="inherited"><a href="mapview/HereMap/toStringShallow.html">toStringShallow</a></li>
<li class="inherited"><a href="mapview/HereMap/toStringShort.html">toStringShort</a></li>
<li class="section-title inherited"><a href="mapview/HereMap-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/HereMap/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">HereMap class</li>
</ol>
<div class="self-name">HereMap</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/HereMap-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>HereMap class</h1></div>
<section class="desc markdown">
<p>Widget that displays a map. To interact with the map, use the
<a href="../mapview/HereMapController-class.html">/sdk-for-flutter-explore-mapview-heremapcontroller-class</a> object that is passed to <a href="../mapview/HereMapCreatedCallback.html">/sdk-for-flutter-explore-mapview-heremapcreatedcallback</a>
Note: Before using this class, <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a> must be already initialized.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="HereMap">
<a href="../mapview/HereMap/HereMap.html">/sdk-for-flutter-explore-mapview-heremap-heremap</a>({Key? key, <a href="../mapview/HereMapCreatedCallback.html">/sdk-for-flutter-explore-mapview-heremapcreatedcallback</a>? onMapCreated, Set&lt;<wbr/>Factory&lt;<wbr/>OneSequenceGestureRecognizer&gt;&gt;? gestureRecognizers, <a href="../mapview/NativeViewMode.html">/sdk-for-flutter-explore-mapview-nativeviewmode</a> mode = NativeViewMode.virtualDisplay, dynamic options})
</dt>
<dd>
          Creates a widget that displays a map.
            <div class="constructor-modifier features">const</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="gestureRecognizers">
<a href="../mapview/HereMap/gestureRecognizers.html">/sdk-for-flutter-explore-mapview-heremap-gesturerecognizers</a>
→ Set&lt;<wbr/>Factory&lt;<wbr/>OneSequenceGestureRecognizer&gt;&gt;?
</dt>
<dd>
  Which gestures should be consumed by the map.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../mapview/HereMap/hashCode.html">/sdk-for-flutter-explore-mapview-heremap-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="key">
<a href="../mapview/HereMap/key.html">/sdk-for-flutter-explore-mapview-heremap-key</a>
→ Key?
</dt>
<dd class="inherited">
  Controls how one widget replaces another widget in the tree.
  <div class="features">finalinherited</div>
</dd>
<dt class="property" id="mode">
<a href="../mapview/HereMap/mode.html">/sdk-for-flutter-explore-mapview-heremap-mode</a>
→ <a href="../mapview/NativeViewMode.html">/sdk-for-flutter-explore-mapview-nativeviewmode</a>
</dt>
<dd>
  Which method of hosting Android native view (the map) will be used.
Default value is <a href="../mapview/NativeViewMode.html">/sdk-for-flutter-explore-mapview-nativeviewmode</a>.
  <div class="features">final</div>
</dd>
<dt class="property" id="onMapCreated">
<a href="../mapview/HereMap/onMapCreated.html">/sdk-for-flutter-explore-mapview-heremap-onmapcreated</a>
→ <a href="../mapview/HereMapCreatedCallback.html">/sdk-for-flutter-explore-mapview-heremapcreatedcallback</a>?
</dt>
<dd>
  Method called when the map is ready to be used.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/HereMap/runtimeType.html">/sdk-for-flutter-explore-mapview-heremap-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="createElement">
<a href="../mapview/HereMap/createElement.html">/sdk-for-flutter-explore-mapview-heremap-createelement</a>(<wbr/>)
    → StatefulElement

</dt>
<dd class="inherited">
  Creates a <code>StatefulElement</code> to manage this widget's location in the tree.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="createState">
<a href="../mapview/HereMap/createState.html">/sdk-for-flutter-explore-mapview-heremap-createstate</a>(<wbr/>)
    → State&lt;<wbr/>StatefulWidget&gt;

</dt>
<dd>
  Creates the mutable state for this widget at a given location in the tree.
  

</dd>
<dt class="callable inherited" id="debugDescribeChildren">
<a href="../mapview/HereMap/debugDescribeChildren.html">/sdk-for-flutter-explore-mapview-heremap-debugdescribechildren</a>(<wbr/>)
    → List&lt;<wbr/>DiagnosticsNode&gt;

</dt>
<dd class="inherited">
  Returns a list of <code>DiagnosticsNode</code> objects describing this node's
children.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="debugFillProperties">
<a href="../mapview/HereMap/debugFillProperties.html">/sdk-for-flutter-explore-mapview-heremap-debugfillproperties</a>(<wbr/>DiagnosticPropertiesBuilder properties)
    → void

</dt>
<dd class="inherited">
  Add additional properties associated with the node.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/HereMap/noSuchMethod.html">/sdk-for-flutter-explore-mapview-heremap-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toDiagnosticsNode">
<a href="../mapview/HereMap/toDiagnosticsNode.html">/sdk-for-flutter-explore-mapview-heremap-todiagnosticsnode</a>(<wbr/>{String? name, DiagnosticsTreeStyle? style})
    → DiagnosticsNode

</dt>
<dd class="inherited">
  Returns a debug representation of the object that is used by debugging
tools and by <code>DiagnosticsNode.toStringDeep</code>.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/HereMap/toString.html">/sdk-for-flutter-explore-mapview-heremap-tostring</a>(<wbr/>{DiagnosticLevel minLevel = DiagnosticLevel.info})
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toStringDeep">
<a href="../mapview/HereMap/toStringDeep.html">/sdk-for-flutter-explore-mapview-heremap-tostringdeep</a>(<wbr/>{String prefixLineOne = '', String? prefixOtherLines, DiagnosticLevel minLevel = DiagnosticLevel.debug, int wrapWidth = 65})
    → String

</dt>
<dd class="inherited">
  Returns a string representation of this node and its descendants.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toStringShallow">
<a href="../mapview/HereMap/toStringShallow.html">/sdk-for-flutter-explore-mapview-heremap-tostringshallow</a>(<wbr/>{String joiner = ', ', DiagnosticLevel minLevel = DiagnosticLevel.debug})
    → String

</dt>
<dd class="inherited">
  Returns a one-line detailed description of the object.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toStringShort">
<a href="../mapview/HereMap/toStringShort.html">/sdk-for-flutter-explore-mapview-heremap-tostringshort</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A short, textual description of this widget.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../mapview/HereMap/operator_equals.html">/sdk-for-flutter-explore-mapview-heremap-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">HereMap class</li>
</ol>
<h5>mapview library</h5>
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
</HTMLBlock>

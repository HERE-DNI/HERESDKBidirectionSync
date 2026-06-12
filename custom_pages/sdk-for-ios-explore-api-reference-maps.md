---
title: "Maps"
slug: "sdk-for-ios-explore-api-reference-maps"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/Maps"></a>
<a title="Maps  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

        Maps  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Maps</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17AnimationDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/AnimationDelegate"></a>
<a class="token" href="#/s:7heresdk17AnimationDelegateP">AnimationDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A delegate for animation events.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-animationdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">AnimationDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14AnimationStateO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/AnimationState"></a>
<a class="token" href="#/s:7heresdk14AnimationStateO">AnimationState</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes the possible states of an animation.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-animationstate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">AnimationState</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13AssetsManagerC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/AssetsManager"></a>
<a class="token" href="#/s:7heresdk13AssetsManagerC">AssetsManager</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Assets manager interface. Can be used to make assets available to the SDK.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-assetsmanager">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">AssetsManager</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AssetsManager</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AssetsManager</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DataAttributesC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/DataAttributes"></a>
<a class="token" href="#/s:7heresdk14DataAttributesC">DataAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Data attributes collection.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-dataattributes">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DataAttributes</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-dataattributesbase">DataAttributesBase</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DataAttributes</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DataAttributes</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22DataAttributesAccessorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/DataAttributesAccessor"></a>
<a class="token" href="#/s:7heresdk22DataAttributesAccessorC">DataAttributesAccessor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Accessor used for manipulating data attributes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-dataattributesaccessor">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DataAttributesAccessor</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-dataattributesbase">DataAttributesBase</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DataAttributesAccessor</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DataAttributesAccessor</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21DataAttributesBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/DataAttributesBuilder"></a>
<a class="token" href="#/s:7heresdk21DataAttributesBuilderC">DataAttributesBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Data attributes collection builder.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-dataattributesbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DataAttributesBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DataAttributesBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DataAttributesBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributeValueC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/DataAttributeValue"></a>
<a class="token" href="#/s:7heresdk18DataAttributeValueC">DataAttributeValue</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Encapsulates a data attribute value.
Supports basic types and arrays of basic types.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-dataattributevalue">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DataAttributeValue</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DataAttributeValue</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DataAttributeValue</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11DashPatternV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DashPattern"></a>
<a class="token" href="#/s:7heresdk11DashPatternV">DashPattern</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a dash pattern for map polyline.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-dashpattern">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DashPattern</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17DoubleTapDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/DoubleTapDelegate"></a>
<a class="token" href="#/s:7heresdk17DoubleTapDelegateP">DoubleTapDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol for handling double tap gestures.
Double-tap gesture occurs after double-tapping on the screen.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-doubletapdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">DoubleTapDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13DrawOrderTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/DrawOrderType"></a>
<a class="token" href="#/s:7heresdk13DrawOrderTypeO">DrawOrderType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the type of map item draw order. Map item rendering behavior is chosen based on the draw order type.</p>
<p>Regardless of a draw order type map items with a higher draw order are drawn on top of map items with a lower draw order.</p>
<p>When having map items in a scene with the same draw order, but with different draw order types
<code><a href="Enums/DrawOrderType.html#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">DrawOrderType.mapSceneAdditionOrderDependent</a></code> and <code><a href="Enums/DrawOrderType.html#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC11IndependentyA2CmF">DrawOrderType.mapSceneAdditionOrderIndependent</a></code>,
<code><a href="Enums/DrawOrderType.html#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">DrawOrderType.mapSceneAdditionOrderDependent</a></code> items will be rendered on top of <code><a href="Enums/DrawOrderType.html#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC11IndependentyA2CmF">DrawOrderType.mapSceneAdditionOrderIndependent</a></code>
ones.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-drawordertype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">DrawOrderType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6EasingC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Easing"></a>
<a class="token" href="#/s:7heresdk6EasingC">Easing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Animation easing representing an easing function to be used during animations.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-easing">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Easing</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Easing</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Easing</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EasingFunctionO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EasingFunction"></a>
<a class="token" href="#/s:7heresdk14EasingFunctionO">EasingFunction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Animation easing functions.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-easingfunction">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EasingFunction</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22GeoCoordinatesKeyframeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoCoordinatesKeyframe"></a>
<a class="token" href="#/s:7heresdk22GeoCoordinatesKeyframeV">GeoCoordinatesKeyframe</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A GeoCoordinatesKeyframe consists of a GeoCoordinates and an animation duration.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-geocoordinateskeyframe">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">GeoCoordinatesKeyframe</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22GeoOrientationKeyframeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoOrientationKeyframe"></a>
<a class="token" href="#/s:7heresdk22GeoOrientationKeyframeV">GeoOrientationKeyframe</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A GeoOrientationKeyframe consists of a GeoOrientation (camera orientation) and an animation duration.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-geoorientationkeyframe">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">GeoOrientationKeyframe</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12GestureStateO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/GestureState"></a>
<a class="token" href="#/s:7heresdk12GestureStateO">GestureState</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the state of the gesture.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-gesturestate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">GestureState</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GestureTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/GestureType"></a>
<a class="token" href="#/s:7heresdk11GestureTypeO">GestureType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enum that represents the type of a gesture.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-gesturetype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">GestureType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GesturesC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Gestures"></a>
<a class="token" href="#/s:7heresdk8GesturesC">Gestures</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Use this class to process touch events from the platform and detect gesture induced actions on the map view.
Please note that this class holds strong references to the gesture delegates.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-gestures">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Gestures</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Gestures</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Gestures</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7HereMapC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/HereMap"></a>
<a class="token" href="#/s:7heresdk7HereMapC">HereMap</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The representation of a dynamic and interactive geographic map.
The map manages a collection of layers of objects and spaces, presents them in a stacked layout and offers the means to focus on a certain area.
The layers, their relation to the objects and spaces, the layout and the representation style is described through a configuration.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-heremap">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">HereMap</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">HereMap</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">HereMap</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12IconProviderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/IconProvider"></a>
<a class="token" href="#/s:7heresdk12IconProviderC">IconProvider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This provider creates icons from a given set of parameters for map content and constraints for
icon dimensions for a particular map scheme. The icon creation currently does not rely on map
data. Therefore, it works without online connection.</p>
<div class="aside aside-note">
<p class="aside-title">Note</p>
    This feature is in BETA state and thus there can be bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.

</div>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-iconprovider">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">IconProvider</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21IconProviderAssetTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/IconProviderAssetType"></a>
<a class="token" href="#/s:7heresdk21IconProviderAssetTypeO">IconProviderAssetType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asset types for loading icons.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-iconproviderassettype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">IconProviderAssetType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20IconProviderCallbacka"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/IconProviderCallback"></a>
<a class="token" href="#/s:7heresdk20IconProviderCallbacka">IconProviderCallback</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A closure of this type can be provided as a callback to be invoked when an icon is received from the <code><a href="sdk-for-ios-explore-api-reference-classes-iconprovider">IconProvider</a></code> in the
<code>UIImage</code> format. The callback provides information about the loaded icon, or an error if one occurred.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">IconProviderCallback</span> <span class="o">=</span> <span class="p">(</span>
    <span class="n">_</span> <span class="nv">icon</span><span class="p">:</span> <span class="kt">UIImage</span><span class="p">?,</span>
    <span class="n">_</span> <span class="nv">iconDescription</span><span class="p">:</span> <span class="kt">String</span><span class="p">?,</span>
    <span class="n">_</span> <span class="nv">error</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-iconprovidererror">IconProviderError</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>icon</em>
</code>
</td>
<td>
<div>
<p>The created icon, or <code>nil</code> if an error occurred.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>iconDescription</em>
</code>
</td>
<td>
<div>
<p>An English description of the created icon. It will be <code>nil</code> if an error occurred.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>error</em>
</code>
</td>
<td>
<div>
<p>The error that occurred, or <code>nil</code> if the icon is loaded successfully.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17IconProviderErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/IconProviderError"></a>
<a class="token" href="#/s:7heresdk17IconProviderErrorO">IconProviderError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Error which indicates why an icon could not be retrieved.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-iconprovidererror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">IconProviderError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11ImageFormatO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ImageFormat"></a>
<a class="token" href="#/s:7heresdk11ImageFormatO">ImageFormat</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Image format.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-imageformat">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ImageFormat</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16JsonStyleFactoryC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/JsonStyleFactory"></a>
<a class="token" href="#/s:7heresdk16JsonStyleFactoryC">JsonStyleFactory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A factory of <code><a href="sdk-for-ios-explore-api-reference-classes-style">Style</a></code> objects from styles defined in JSON format.
For more details see Custom Layer Style Reference in the documentation.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-jsonstylefactory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">JsonStyleFactory</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">JsonStyleFactory</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">JsonStyleFactory</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25KeyframeInterpolationModeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/KeyframeInterpolationMode"></a>
<a class="token" href="#/s:7heresdk25KeyframeInterpolationModeO">KeyframeInterpolationMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies type of interpolation performed between keyframes.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-keyframeinterpolationmode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">KeyframeInterpolationMode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7LineCapO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LineCap"></a>
<a class="token" href="#/s:7heresdk7LineCapO">LineCap</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Determines the cap (line ending) style.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-linecap">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LineCap</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LineTileDataSourceC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineTileDataSource"></a>
<a class="token" href="#/s:7heresdk18LineTileDataSourceC">LineTileDataSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Line tile data source allows the rendering engine access to user managed data sets of
geodetic lines and their attributes through a <code><a href="sdk-for-ios-explore-api-reference-protocols-linetilesource">LineTileSource</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-linetiledatasource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LineTileDataSource</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineTileDataSource</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineTileDataSource</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LineTileSourceP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/LineTileSource"></a>
<a class="token" href="#/s:7heresdk14LineTileSourceP">LineTileSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A source of geodetic line tiles.
Lines provided by an implementation must be clipped to the boundaries of the requested tile.
The implementations must be thread-safe.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-linetilesource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">LineTileSource</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-tilesource">TileSource</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31LineTileSourceLoadResultHandlerP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/LineTileSourceLoadResultHandler"></a>
<a class="token" href="#/s:7heresdk31LineTileSourceLoadResultHandlerP">LineTileSourceLoadResultHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Result handler of a load tile request.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-linetilesourceloadresulthandler">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">LineTileSourceLoadResultHandler</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LocationIndicator"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC">LocationIndicator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Graphical object to represent the location of the user on the map.</p>
<p>It is either a green dot for pedestrian style or a triangular arrow for vehicle navigation style.
This style can be changed by <code><a href="Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC08locationC5StyleAC0cE0Ovp">LocationIndicator.locationIndicatorStyle</a></code></p>
<p>The location is made available to an instance of this class by calling <code>LocationIndicator.updateLocation(Location)</code> or
<code>LocationIndicator.updateLocation(Location, MapCameraUpdate)</code>.</p>
<p>Use <code><a href="Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC6enable3foryAA11MapViewBase_p_tF">LocationIndicator.enable(...)</a></code> to add this object to the map and <code><a href="Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC7disableyyF">LocationIndicator.disable(...)</a></code> to remove it.</p>
<p>Note: The LocationIndicator is always rendered at a fixed altitude near 0. Changing the MapCamera
to look at geographic coordinates with an altitude that is higher can cause the following behavior: If the
MapCamera angle is tilted and altitude is too high, the LocationIndicator can unexpectedly
disappear from the viewport due to the new perspective.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-locationindicator">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LocationIndicator</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LocationIndicator</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LocationIndicator</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LongPressDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/LongPressDelegate"></a>
<a class="token" href="#/s:7heresdk17LongPressDelegateP">LongPressDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol for handling long-press gestures.
Long-press gesture occurs after tapping and holding the finger for a long time on the screen.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-longpressdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">LongPressDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapArrowC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapArrow"></a>
<a class="token" href="#/s:7heresdk8MapArrowC">MapArrow</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A visual representation of an arrow on the map. It consists of a tail - a polyline with an arbitrary
number of points - and a head at its end.</p>
<p>The map arrows are only visible on zoom levels &gt;= 13.</p>
<p>Altitude component of <code><a href="sdk-for-ios-explore-api-reference-structs-geopolyline">GeoPolyline</a></code>‘s vertices is ignored.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-maparrow">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapArrow</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapArrow</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapArrow</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCamera"></a>
<a class="token" href="#/s:7heresdk9MapCameraC">MapCamera</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the camera looking onto the map view.</p>
<p>Each map instance has exactly one camera that is used to manipulate
the way the map is displayed.</p>
<p>Any updates to the state of the camera will be applied while drawing the next map view frame
and the current state of the camera reflects what is currently drawn inside the map view.</p>
<p>Note: The camera can be configured and positioned even before a map scene is loaded for the first time.
This allows for pre-setting the desired camera position, orientation, and zoom level, which will be
applied once the map scene becomes available.</p>
<p><b>Camera Model</b></p>
<p><i>Camera Concepts and Units</i></p>
<p>By default, HERE SDK uses an idealized Earth globe with a 3D-capable camera model. Being a 3D camera model means that the
world position can be freely specified in geodetic 3D space (i.e. Earth centric) and the orientation can be freely changed around
two axes - bearing (also known as head) and tilt (also known as pitch).</p>
<p>The camera supports the look-at target with orientation on the ground way of setting up the camera in space. The camera is placed
so that it looks at a specific geo-coordinates (placed at the <code>principal point</code>) from a given orientation and distance.</p>
<ul>
<li>the look-at target in geo-coordinates (latitude, longitude) in degrees and an <code>altitude</code> in meters above MSL (mean sea level) at the <code>principal point</code></li>
<li>the <code>orientation</code> at the look-at target</li>
<li>the distance of the camera from the look-at target, given as <code>distance</code> in meters or as <code>zoom-level</code></li>
</ul>
<p><i>Getting the current camera state</i></p>
<p>The current camera state can be obtained by the <code><a href="Classes/MapCamera.html#/s:7heresdk9MapCameraC5stateAC5StateVvp">MapCamera.state</a></code> call. It contains information about the camera look-at target (geo-coordinates and orientation) in geodetic space.
The values are returned for the current <code>principal point</code>. This can lead to surprising or unexpected values in cases where the camera position/orientation was specified for another screen point,
e.g. when using <code>MapCameraUpdateFactory.lookAt(GeoBox)</code> with a view rectangle, whose center does not coincide with the <code>principal point</code>.  In this case, the geo-coordinates of the
look-at target will differ from the center of the geo-box used in the <code>lookAt</code> call.</p>
<p><i>Geo coordinates</i></p>
<p>Geo-coordinates are given in degrees and follow the common nomenclature of positive northern latitudes and positive eastern longitudes.</p>
<p><i>Altitude</i></p>
<p>When <code>altitude</code> is specified, it is always in meters above mean sea level (MSL).
If this value is invalid (not-a-number) or not specified, then the terrain height at the given geo-coordinates will be looked up from the map.
This is especially interesting in cases where terrain elevation is used within the map display.</p>
<p><i>Distance vs zoom-level vs scale</i></p>
<p>Map camera <code>distance</code>, <code>zoom-level</code> and <code>scale</code> determine how much of the world is visible on the HERE map. <code>Distance</code>, <code>zoom-level</code> and <code>scale</code> are
directly connected and changing one will automatically change the others as well (except for <code>distance</code>/<code>scale</code> changes that map to <code>zoom-level</code> values &lt; 0 or &gt; 23).</p>
<ul>
<li><code>distance</code>: the distance from the camera to the look-at target on the surface of the Earth, in meters</li>
<li><code>zoom-level</code>: the map zoom level, in the range [0, 3]. The relation between the width of the equator in logical pixels <code>w</code> and the zoom level <code>z</code> is: <code>w = 256 * 2^(z)</code></li>
<li><code>scale</code>: the scale of the map at the look-at target in meters on screen per meters on Earth. So a scale of 0.001 shows 10 meters on Earth within 1 cm on screen.</li>
</ul>
<p>The following mapping represents the <code>zoom-level</code> values:</p>
<table><thead>
<tr>
<th>zoom-level</th>
<th style="text-align: center">~ scale on screen (130dpi)</th>
<th style="text-align: center">width of the equator in logical pixels</th>
<th style="text-align: center">what can be seen</th>
</tr>
</thead><tbody>
<tr>
<td>0</td>
<td style="text-align: center">1:800 million</td>
<td style="text-align: center">256</td>
<td style="text-align: center">Earth</td>
</tr>
<tr>
<td>1</td>
<td style="text-align: center">1:400 million</td>
<td style="text-align: center">512</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>2</td>
<td style="text-align: center">1:200 million</td>
<td style="text-align: center">1024</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>3</td>
<td style="text-align: center">1:100 million</td>
<td style="text-align: center">2048</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>4</td>
<td style="text-align: center">1:50 million</td>
<td style="text-align: center">4096</td>
<td style="text-align: center">A continent</td>
</tr>
<tr>
<td>5</td>
<td style="text-align: center">1:25 million</td>
<td style="text-align: center">8192</td>
<td style="text-align: center">Large roads</td>
</tr>
<tr>
<td>6</td>
<td style="text-align: center">1:12 million</td>
<td style="text-align: center">16384</td>
<td style="text-align: center">Large rivers</td>
</tr>
<tr>
<td>7</td>
<td style="text-align: center">1:6 million</td>
<td style="text-align: center">32768</td>
<td style="text-align: center">A country</td>
</tr>
<tr>
<td>8</td>
<td style="text-align: center">1:3 million</td>
<td style="text-align: center">65536</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>9</td>
<td style="text-align: center">1:1 million</td>
<td style="text-align: center">131072</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>10</td>
<td style="text-align: center">1:780 thousand</td>
<td style="text-align: center">262144</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>11</td>
<td style="text-align: center">1:390 thousand</td>
<td style="text-align: center">524288</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>12</td>
<td style="text-align: center">1:195 thousand</td>
<td style="text-align: center">1048576</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>13</td>
<td style="text-align: center">1:100 thousand</td>
<td style="text-align: center">2097152</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>14</td>
<td style="text-align: center">1:50 thousand</td>
<td style="text-align: center">4194304</td>
<td style="text-align: center">A city</td>
</tr>
<tr>
<td>15</td>
<td style="text-align: center">1:25 thousand</td>
<td style="text-align: center">8388608</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>16</td>
<td style="text-align: center">1:12 thousand</td>
<td style="text-align: center">16777216</td>
<td style="text-align: center">Buildings</td>
</tr>
<tr>
<td>17</td>
<td style="text-align: center">1:6 thousand</td>
<td style="text-align: center">33554432</td>
<td style="text-align: center">Landmarks</td>
</tr>
<tr>
<td>18</td>
<td style="text-align: center">1:3 thousand</td>
<td style="text-align: center">67108864</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>19</td>
<td style="text-align: center">1:1 thousand</td>
<td style="text-align: center">134217728</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>20</td>
<td style="text-align: center">1:7 hundred</td>
<td style="text-align: center">268435456</td>
<td style="text-align: center">Streets</td>
</tr>
<tr>
<td>21</td>
<td style="text-align: center">1:3 hundred</td>
<td style="text-align: center">536870912</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>22</td>
<td style="text-align: center">1:1 hundred</td>
<td style="text-align: center">1073741824</td>
<td style="text-align: center"></td>
</tr>
<tr>
<td>23</td>
<td style="text-align: center">1:95</td>
<td style="text-align: center">2147483648</td>
<td style="text-align: center"></td>
</tr>
</tbody></table>
<p><i>Orientation</i></p>
<p>The camera <code>orientation</code> is composed of two parts:</p>
<ul>
<li><code>bearing</code>: also known as azimuth, the view direction in clockwise degrees; 0° = north, 90° = east, 180° = south, 270° = west</li>
<li><code>tilt</code>: the angle in degrees from the vertical that the camera is looking down at the Earth; 0° = straight down.</li>
</ul>
<p><i>Changing the Camera</i></p>
<p>All changes to the camera are encapsulated in camera updates that are created using the methods in the <code><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdatefactory">MapCameraUpdateFactory</a></code> class.</p>
<p>These updates can then be applied to the <code><a href="sdk-for-ios-explore-api-reference-classes-heremap">HereMap</a></code> using <code><a href="Classes/MapCamera.html#/s:7heresdk9MapCameraC11applyUpdateyyAA0bcE0CF">MapCamera.applyUpdate(...)</a></code>.</p>
<p>Camera updates are queued and executed when the next frame is rendered. They are executed in the order in which they were applied.</p>
<p><i>Animating the Camera</i></p>
<p>Camera updates can be animated by first creating a camera animation using the methods in the <code><a href="sdk-for-ios-explore-api-reference-classes-mapcameraanimationfactory">MapCameraAnimationFactory</a></code> class and then applying this
animation to the <code><a href="sdk-for-ios-explore-api-reference-classes-heremap">HereMap</a></code> using <code>MapCamera.startAnimation(MapCameraAnimation, AnimationDelegate)</code>.</p>
<p>Only one camera animation for one camera component at a time is supported. Applying a new animation will cancel the active animation before the new one is started.
The start position in this case is where ever the active animation happened to be at the time. Different components are camera state (<code>target pose</code> and <code>distance/zoom level/scale</code>)
and camera projection (<code>field of view</code>, <code>focal length</code> and <code>principal point</code>).</p>
<p>The running animations can also be canceled using <code><a href="Classes/MapCamera.html#/s:7heresdk9MapCameraC16cancelAnimationsyyF">MapCamera.cancelAnimations(...)</a></code> or individual ones using <code><a href="Classes/MapCamera.html#/s:7heresdk9MapCameraC15cancelAnimationyyAA0bcE0CF">MapCamera.cancelAnimation(...)</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapcamera">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCamera</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCamera</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCamera</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCameraAnimation"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC">MapCameraAnimation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An animation that can be applied to a <code><a href="sdk-for-ios-explore-api-reference-classes-mapcamera">MapCamera</a></code>.
Creation is done via <code><a href="sdk-for-ios-explore-api-reference-classes-mapcameraanimationfactory">MapCameraAnimationFactory</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapcameraanimation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCameraAnimation</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraAnimation</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraAnimation</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25MapCameraAnimationFactoryC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCameraAnimationFactory"></a>
<a class="token" href="#/s:7heresdk25MapCameraAnimationFactoryC">MapCameraAnimationFactory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Factory for creating MapCameraAnimation objects to change map’s camera over time.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapcameraanimationfactory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCameraAnimationFactory</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraAnimationFactory</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraAnimationFactory</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17MapCameraDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/MapCameraDelegate"></a>
<a class="token" href="#/s:7heresdk17MapCameraDelegateP">MapCameraDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol for objects that want to get updates whenever the map is redrawn after
camera parameters change.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-mapcameradelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">MapCameraDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCameraKeyframeTrack"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC">MapCameraKeyframeTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Stores keyframes for interpolation of a camera property using a specific easing function
and interpolation mode. Can only hold keyframes of a single type.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapcamerakeyframetrack">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCameraKeyframeTrack</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraKeyframeTrack</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraKeyframeTrack</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraLimitsC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCameraLimits"></a>
<a class="token" href="#/s:7heresdk15MapCameraLimitsC">MapCameraLimits</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Controls constraints on map camera parameters.</p>
<p>When constraints are set, they are enforced for current camera state
and for all future changes to the camera.</p>
<p>When setting, limits are applied on next rendering loop.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapcameralimits">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCameraLimits</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraLimits</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraLimits</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapCameraUpdateC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCameraUpdate"></a>
<a class="token" href="#/s:7heresdk15MapCameraUpdateC">MapCameraUpdate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An update that can be applied to the map camera.
Creation is done via <code><a href="sdk-for-ios-explore-api-reference-classes-mapcameraupdatefactory">MapCameraUpdateFactory</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapcameraupdate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCameraUpdate</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraUpdate</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraUpdate</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraUpdateFactoryC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCameraUpdateFactory"></a>
<a class="token" href="#/s:7heresdk22MapCameraUpdateFactoryC">MapCameraUpdateFactory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Factory for creating MapCameraUpdate to change map’s camera.</p>
<p>For some factory methods you can apply an additional padding in pixels by setting a
<code>viewRectangle</code> parameter based on the current size of the map view:</p>
<pre class="highlight swift"><code><span class="k">let</span> <span class="nv">leftPaddingInPixels</span> <span class="o">=</span> <span class="mi">5</span>
<span class="k">let</span> <span class="nv">rightPaddingInPixels</span> <span class="o">=</span> <span class="mi">5</span>
<span class="k">let</span> <span class="nv">topPaddingInPixels</span> <span class="o">=</span> <span class="mi">5</span>
<span class="k">let</span> <span class="nv">bottomPaddingInPixels</span> <span class="o">=</span> <span class="mi">5</span>
<span class="k">let</span> <span class="nv">horizontalPaddingInPixels</span> <span class="o">=</span> <span class="n">leftPaddingInPixels</span> <span class="o">+</span> <span class="n">rightPaddingInPixels</span>
<span class="k">let</span> <span class="nv">verticalPaddingInPixels</span> <span class="o">=</span> <span class="n">topPaddingInPixels</span> <span class="o">+</span> <span class="n">bottomPaddingInPixels</span>

<span class="k">let</span> <span class="nv">origin</span> <span class="o">=</span> <span class="kt">Point2D</span><span class="p">(</span><span class="n">leftPaddingInPixels</span><span class="p">,</span> <span class="n">topPaddingInPixels</span><span class="p">)</span>
<span class="k">let</span> <span class="nv">sizeInPixels</span> <span class="o">=</span> <span class="kt">Size2D</span><span class="p">(</span><span class="nv">width</span><span class="p">:</span> <span class="n">mapView</span><span class="o">.</span><span class="n">viewportSize</span><span class="o">.</span><span class="n">width</span> <span class="o">-</span> <span class="n">horizontalPaddingInPixels</span><span class="p">,</span> <span class="nv">height</span><span class="p">:</span> <span class="n">mapView</span><span class="o">.</span><span class="n">viewportSize</span><span class="o">.</span><span class="n">height</span> <span class="o">-</span> <span class="n">verticalPaddingInPixels</span><span class="p">)</span>
<span class="k">let</span> <span class="nv">paddedViewRectangle</span> <span class="o">=</span> <span class="kt">Rectangle2D</span><span class="p">(</span><span class="nv">origin</span><span class="p">:</span> <span class="n">origin</span><span class="p">,</span> <span class="nv">size</span><span class="p">:</span> <span class="n">sizeInPixels</span><span class="p">)</span>
</code></pre>
<p>The origin indicates the top-left corner of the rectangle. An origin of (0, 0) indicates
also the top-left corner of the map’s viewport.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapcameraupdatefactory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCameraUpdateFactory</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraUpdateFactory</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraUpdateFactory</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentCategoryO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MapContentCategory"></a>
<a class="token" href="#/s:7heresdk18MapContentCategoryO">MapContentCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type representing map content categories.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-mapcontentcategory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MapContentCategory</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapContentSettings"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC">MapContentSettings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides settings regarding map data which are applied globally to all map views. The settings
can already be changed before a map view instance is created.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapcontentsettings">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapContentSettings</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapContentSettings</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapContentSettings</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapContentTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MapContentType"></a>
<a class="token" href="#/s:7heresdk14MapContentTypeO">MapContentType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Content types supported by the map.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-mapcontenttype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MapContentType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapContext"></a>
<a class="token" href="#/s:7heresdk10MapContextC">MapContext</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>MapContext is the rendering engine and the context in which virtual geographic maps get rendered.</p>
<p>It runs the render loop or offers the means for the user to run a custom one.</p>
<p>Data sources, assets and virtual maps can be attached to the context. A virtual map can only
render data from sources attached to the same context.</p>
<p>The graphics backend to be used by the engine can be choosen by the user or a platform suitable
one can be automatically selected internally. Only one graphics backend can be active and once
selected it cannot be changed.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapcontext">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapContext</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapContext</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapContext</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MapError"></a>
<a class="token" href="#/s:7heresdk8MapErrorO">MapError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents various errors that could occur from map related operations.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-maperror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MapError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MapFeatures"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV">MapFeatures</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Holds constants for map features, to be used with
<code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> and <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC15disableFeaturesyySaySSGF">MapScene.disableFeatures(...)</a></code>.</p>
<p>See <code><a href="sdk-for-ios-explore-api-reference-structs-mapfeaturemodes">MapFeatureModes</a></code> for constants representing feature modes.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-mapfeatures">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapFeatures</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MapFeatureModes"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV">MapFeatureModes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Holds constants for map feature modes, to be used with <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code>.</p>
<p>Use <code><a href="Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV11defaultModeSSvpZ">MapFeatureModes.defaultMode</a></code> to enable a feature with its default mode.</p>
<p>Note: The default mode is defined by the currently loaded map scene configuration and
may vary per <code><a href="sdk-for-ios-explore-api-reference-enums-mapscheme">MapScheme</a></code>. The currently active features and modes can be inspected
using <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF">MapScene.getActiveFeatures(...)</a></code> after the scene is loaded.</p>
<p>See <code><a href="sdk-for-ios-explore-api-reference-structs-mapfeatures">MapFeatures</a></code> for constants representing the feature names.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-mapfeaturemodes">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapFeatureModes</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapIdleDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/MapIdleDelegate"></a>
<a class="token" href="#/s:7heresdk15MapIdleDelegateP">MapIdleDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Used to detect when the map becomes idle or busy.</p>
<p>Map is considered busy when its state changes (for example as a result of camera manipulation)
and/or when it requires a redraw (for example, as a result of map data being downloaded).</p>
<p>Map is considered idle when current state is fully rendered and no further
redraws are necessary.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-mapidledelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">MapIdleDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapImageC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapImage"></a>
<a class="token" href="#/s:7heresdk8MapImageC">MapImage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a drawable resource that can be used by a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code>, <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker3d">MapMarker3D</a></code> or <code><a href="sdk-for-ios-explore-api-reference-classes-mapimageoverlay">MapImageOverlay</a></code> to be shown on the map.
Supported formats are listed in <code><a href="sdk-for-ios-explore-api-reference-enums-imageformat">ImageFormat</a></code>.
SVG format allows custom fonts in text using font-family attribute by prior registration via <code>AssetsManager.registerFont</code>.</p>
<p>It is recommended to associate a resource with a single <code>MapImage</code> instance in order to enable
resource sharing and reduce the amount of needed memory.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapimage">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapImage</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapImage</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapImage</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapImageOverlayC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapImageOverlay"></a>
<a class="token" href="#/s:7heresdk15MapImageOverlayC">MapImageOverlay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>MapImageOverlay</code> is used to draw images over the map, at a view coordinate inside the map viewport.</p>
<p>The image to be displayed is represented by a <code><a href="sdk-for-ios-explore-api-reference-classes-mapimage">MapImage</a></code> object.
By default, the overlay is centered on the given view coordinate.</p>
<p>The resulting viewport area covered by the overlay is computed out of the overlay’s view coordinate,
the anchor point and the image size. The overlay subareas that fall outside of the map viewport get clipped.</p>
<p>To display the map overlay, it needs to be added to the scene using <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC03addB12ImageOverlayyyAA0beF0CF">MapScene.addMapImageOverlay(...)</a></code>.
To stop displaying it, remove it from the scene using <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC06removeB12ImageOverlayyyAA0beF0CF">MapScene.removeMapImageOverlay(...)</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapimageoverlay">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapImageOverlay</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapImageOverlay</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapImageOverlay</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MapItemKeyFrameTrackC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapItemKeyFrameTrack"></a>
<a class="token" href="#/s:7heresdk20MapItemKeyFrameTrackC">MapItemKeyFrameTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Stores keyframes for interpolation of a map item property using a specific
easing function and interpolation mode.</p>
<p>The keyframe track object is used to create animations,
see <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarkeranimation">MapMarkerAnimation</a></code> and <code><a href="sdk-for-ios-explore-api-reference-classes-mappolylineanimation">MapPolylineAnimation</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapitemkeyframetrack">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapItemKeyFrameTrack</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapItemKeyFrameTrack</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapItemKeyFrameTrack</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21MapItemRepresentationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapItemRepresentation"></a>
<a class="token" href="#/s:7heresdk21MapItemRepresentationC">MapItemRepresentation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Base class to represent visual style of particular map items.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapItemRepresentation</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapItemRepresentation</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapItemRepresentation</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapLayerC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapLayer"></a>
<a class="token" href="#/s:7heresdk8MapLayerC">MapLayer</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Interface for managing a map layer.
A map layer can be created by using the <code><a href="sdk-for-ios-explore-api-reference-classes-maplayerbuilder">MapLayerBuilder</a></code>. At creation, the layer
gets added to a map. The layer gets removed from the map upon instance destruction.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-maplayer">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapLayer</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayer</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayer</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapLayerBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapLayerBuilder"></a>
<a class="token" href="#/s:7heresdk15MapLayerBuilderC">MapLayerBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>MapLayerBuilder is used to add layers to a map to visualise a dataset in a
programmatic way without defining it upfront in the configuration files.</p>
<p>For example, after loading a scene configuration file, the renderer is setup to draw layers in the
following order:</p>
<ul>
<li>background</li>
<li>water</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
<p>Rendering order of elements in
a single map layer can be controlled with categories. Layer names are unique, and category names have
to be unique within a layer. The layer’s default, main category is unnamed.</p>
<p>The concept of ‘category’ is tightly linked to styling. The idea behind category is that
one should be able to style separately elements in a map layer. Take, for instance, roads.
If one wants to style separately the bridges it will create a category ‘bridges’ and style
it accordingly in the style file. If the user does not intend to or cannot style elements of
the layer differently then it should opt for a layer with only the default category (e.g.
for a raster layer, only the default category makes sense, since the layer has no other
stylable elements apart from the raster image).</p>
<p>A new layer called ‘zone’ and its category ‘background’ can be added dynamically so that the
rendering order gets modified in the following way:</p>
<ul>
<li>background</li>
<li>water</li>
<li>zone:background</li>
<li>zone</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
<p>This could be achieved with the help of the MapLayerPriorityBuilder and the MapLayerBuilder as in the
following example:</p>
<pre class="highlight swift"><code>  <span class="k">let</span> <span class="nv">layerPriority</span> <span class="o">=</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"water"</span><span class="p">)</span> <span class="c1">// places main category after 'water'</span>
     <span class="o">.</span><span class="nf">withCategory</span><span class="p">(</span><span class="s">"background"</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"water"</span><span class="p">)</span> <span class="c1">// places 'background' category after 'water' and before the</span>
                                         <span class="c1">// layer's main category.</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">();</span>

  <span class="k">let</span> <span class="nv">layer</span> <span class="o">=</span> <span class="kt">MapLayerBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">withDataSource</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"DataSourceName"</span><span class="p">,</span> <span class="nv">contentType</span><span class="p">:</span> <span class="kt">MapContentType</span><span class="o">.</span><span class="n">line</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">forMap</span><span class="p">(</span><span class="n">map</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withName</span><span class="p">(</span><span class="s">"zone"</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withPriority</span><span class="p">(</span><span class="n">layerPriority</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">();</span>
</code></pre>
<p>In case no layer priority or an empty one is provided, or if a reference layer-category pair is not
present in the rendering order, the layer is going to be rendered last with respect to the rendering
order at the time of its creation.</p>
<p>Due to current limitations, the MapLayerPriority assignment is not implemented for point map layers.
All labels will be rendered within the “labels” layer, defined in the scene configuration file.
By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed.
The following categories can be used to have a different behaviour:</p>
<ul>
<li>‘custom-labels’ A label should be rendered first, is allowed to overlap with other labels of
the same category and block map labels.</li>
<li>‘custom-labels-no-self-overlap’ A label should be rendered after ‘custom-labels’, is not allowed
to overlap with other labels of the same categoty and block map labels.</li>
<li>‘custom-labels-overlap-all’ A label should be rendered last, is allowed to overlap all
predefined categories, also map labels.
These categories are configured accordingly in the basic map
scene configurations.
Category assignment to features can be done in the style based on data attributes. The category
assignment can be done for all types of content: point, line, polygon.</li>
</ul>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-maplayerbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapLayerBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapLayerPriorityC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapLayerPriority"></a>
<a class="token" href="#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>MapLayerPriority class. Instances are configured and created via a <code><a href="sdk-for-ios-explore-api-reference-classes-maplayerprioritybuilder">MapLayerPriorityBuilder</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapLayerPriority</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerPriority</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerPriority</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerPriorityBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapLayerPriorityBuilder"></a>
<a class="token" href="#/s:7heresdk23MapLayerPriorityBuilderC">MapLayerPriorityBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer
and its categories, relative to other layers or layer-category pairs.</p>
<p>Map layers are rendered in an order according to specified priorities. Rendering order of elements in
a single map layer can be controlled with categories. Layer names are unique, and category names have
to be unique within a layer. The layer’s default, main category is unnamed.</p>
<p>The concept of ‘category’ is tightly linked to styling. The idea behind category is that
one should be able to style separately elements in a map layer. Take, for instance, roads.
If one wants to style separately the bridges it will create a category ‘bridges’ and style
it accordingly in the style file. If the user does not intend to or cannot style elements
of the layer diffenrently then it should opt for a layer with only the default category (e.g.
raster layer).</p>
<p>One way to define layers’ priorities is by using a layer priority list in the scene configuration.</p>
<p>For example, a priority list in a scene configuration could define:</p>
<ul>
<li>background</li>
<li>water</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
<p>This means layer “background” is rendered first. Next up is layer “water”. Then category “outline” of
layer “roads”, followed by the main category of layer “roads”. Layer “labels” is then rendered last.</p>
<p><p>
Now let’s consider a newly created layer ‘zone’ and its categories:</p>
<ul>
<li>zone</li>
<li>zone:background</li>
<li>zone:lines-outline</li>
<li>zone:lines</li>
</ul>
<p>The user wants to alter the rendering order so that it looks like:</p>
<ul>
<li>background</li>
<li>water</li>
<li>zone:background</li>
<li>zone</li>
<li>road:outline</li>
<li>road</li>
<li>zone:lines-outline</li>
<li>zone:lines</li>
<li>labels</li>
</ul>
<p>This could be achieved with the help of the MapLayerPriorityBuilder and a sequence of calls to its
<code>renderedBeforeLayer()</code> and <code>renderedAfterLayer()</code> member functions.</p>
<p>Note that the order of calls matters and one can use a previously defined layer or category
as a reference:</p>
<pre class="highlight swift"><code>  <span class="k">let</span> <span class="nv">zoneLayerPriority</span> <span class="o">=</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">()</span>
      <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"water"</span><span class="p">)</span>     <span class="c1">// places "zone" after "water"</span>
                                              <span class="c1">// in the rendering order</span>
      <span class="o">.</span><span class="nf">withCategory</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"background"</span><span class="p">)</span>
      <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"water"</span><span class="p">)</span>     <span class="c1">// places "zone:background" after "water"</span>
                                              <span class="c1">// in the rendering order and thus shifts</span>
                                              <span class="c1">// "zone" to be rendered later</span>
      <span class="o">.</span><span class="nf">withCategory</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"lines-outline"</span><span class="p">)</span>
      <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"road"</span><span class="p">)</span>      <span class="c1">// places "zone:lines-outline" after "road"</span>
                                              <span class="c1">// in the rendering order</span>
      <span class="o">.</span><span class="nf">withCategory</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"lines"</span><span class="p">)</span>
      <span class="o">.</span><span class="nf">renderedAfterLayer</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"zone"</span><span class="p">,</span> <span class="nv">categoryName</span><span class="p">:</span> <span class="s">"lines-outline"</span><span class="p">)</span> <span class="c1">// places "zone:lines" after</span>
                                                                        <span class="c1">// "zone:lines-outline" in the rendering order</span>
      <span class="o">.</span><span class="nf">build</span><span class="p">();</span>

  <span class="n">zoneLayer</span><span class="o">.</span><span class="nf">setPriority</span><span class="p">(</span><span class="n">zoneLayerPriority</span><span class="p">);</span>  <span class="c1">// applies the priority to the zone layer</span>
                                            <span class="c1">// and its categories in one single operation.</span>
</code></pre>
<p>In case an empty MapLayerPriority without any ordering commands is built, it is assumed that the target layer
is going to be rendered last.</p>
<p>Due to a current limitation for point map layers, the mentioned APIs to control the rendering
order are not implemented. All labels will be rendered within the “labels” layer, defined in
the scene configuration file.
By default, all labels rendered by a point map layer are rendered last and no overlapping is
allowed. The following categories can be used to have a different behaviour:</p>
<ul>
<li>‘custom-labels’ A label should be rendered first, is allowed to overlap with other labels of
the same category and block map labels.</li>
<li>‘custom-labels-no-self-overlap’ A label should be rendered after ‘custom-labels’, is not allowed
to overlap with other labels of the same categoty and block map labels.</li>
<li>‘custom-labels-overlap-all’ A label should be rendered last, is allowed to overlap all
predefined categories, also map labels.
These categories are configured accordingly in the basic map
scene configurations.
Category assignment to features can be done in the style based on data attributes. The category
assignment can be done for all types of data: points, lines, polygons.</li>
</ul>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-maplayerprioritybuilder">See more</a>
</p></div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapLayerPriorityBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk08MapLayerB29MeasureDependentStorageLevelsC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapLayerMapMeasureDependentStorageLevels"></a>
<a class="token" href="#/s:7heresdk08MapLayerB29MeasureDependentStorageLevelsC">MapLayerMapMeasureDependentStorageLevels</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides a mapping between a MapLayer map measure to datasource storage level.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-maplayermapmeasuredependentstoragelevels">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapLayerMapMeasureDependentStorageLevels</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerMapMeasureDependentStorageLevels</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLayerMapMeasureDependentStorageLevels</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MapLayerVisibilityRangeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MapLayerVisibilityRange"></a>
<a class="token" href="#/s:7heresdk23MapLayerVisibilityRangeV">MapLayerVisibilityRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A layer’s visibility along a zoom level range.
The range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-maplayervisibilityrange">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapLayerVisibilityRange</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapMarkerCluster"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC">MapMarkerCluster</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Groups map markers and enables their clustering to reduce visual clutter when there are many of
them in a small area.</p>
<p>The markers that are close to each other are replaced by a single cluster marker. Cluster groups
are generated based on geographical distance between objects, not based on screen space collision.
Hence it is possible, that cluster markers can overlap.</p>
<p>The markers can be added to a cluster or to a scene, but not to both. To display the cluster on the
map, add it to the scene using <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC03addB13MarkerClusteryyAA0beF0CF">MapScene.addMapMarkerCluster(...)</a></code>. The display of a cluster is only
guaranteed in case its origin is within the viewport. At the moment, this is a known limitation
that mostly affects clusters which are visually large and cover a sizeable part of the viewport.</p>
<p>Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapmarkercluster">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapMarkerCluster</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarkerCluster</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarkerCluster</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapMeasureRangeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MapMeasureRange"></a>
<a class="token" href="#/s:7heresdk15MapMeasureRangeV">MapMeasureRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A map measure range.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-mapmeasurerange">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapMeasureRange</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19MapObjectDescriptorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapObjectDescriptor"></a>
<a class="token" href="#/s:7heresdk19MapObjectDescriptorC">MapObjectDescriptor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Interface represents descriptor of a pickable map object.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapobjectdescriptor">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapObjectDescriptor</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapObjectDescriptor</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapObjectDescriptor</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapProjectionO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MapProjection"></a>
<a class="token" href="#/s:7heresdk13MapProjectionO">MapProjection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The map projection used for rendering.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-mapprojection">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MapProjection</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapSceneLightsC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapSceneLights"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC">MapSceneLights</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Manage the lights and their attributes in a scene.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapscenelights">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapSceneLights</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapSceneLights</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapSceneLights</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19MapSceneLoadOptionsC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapSceneLoadOptions"></a>
<a class="token" href="#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the configuration options for loading a map scene.
This class combines both the scene source (MapScheme or configuration file) and
optional settings like features, watermark style and overriding map style.</p>
<p>It is left empty intentionally. Use <code><a href="sdk-for-ios-explore-api-reference-classes-mapsceneloadoptionsbuilder">MapSceneLoadOptionsBuilder</a></code> to create instances of this class.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapSceneLoadOptions</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapSceneLoadOptions</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapSceneLoadOptions</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapSceneLoadOptionsBuilder"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderC">MapSceneLoadOptionsBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder for creating <code><a href="Maps.html#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a></code> instances.
This builder ensures that either a MapScheme or a configuration file is set, but not both.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapsceneloadoptionsbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapSceneLoadOptionsBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapSceneLoadOptionsBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapSceneLoadOptionsBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapMarker"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC">MapMarker</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>MapMarker</code> is used to draw images on the map, for example to mark a specific location.
By default, the marker is centered on the given geographic coordinates.
Markers keep their size regardless of the current zoom level of the map view.</p>
<p>The image to be displayed is represented by <code><a href="sdk-for-ios-explore-api-reference-classes-mapimage">MapImage</a></code> object. For performance reasons,
it is highly recommended to reuse a single instance of the image when creating multiple
identical markers.</p>
<p>To display the map marker, it needs to be added to the scene using <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC03addB6MarkeryyAA0bE0CF">MapScene.addMapMarker(...)</a></code>.
To stop displaying it, remove it from the scene using <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC06removeB6MarkeryyAA0bE0CF">MapScene.removeMapMarker(...)</a></code>.</p>
<p>The display of a map marker is only guaranteed in case its origin is within the viewport.
At the moment, this is a known limitation that mostly affects map markers which are visually
large and cover a sizeable part of the viewport.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapMarkers API to add a very large number of markers
(several thousands, especially 10000+) is not recommended. Adding this many markers will have a
negative impact on the performance leading to stuttering of the app and lower frame rates.
To work around this limitation the following approach can be used:
Register to map camera updates using <code><a href="Classes/MapCamera.html#/s:7heresdk9MapCameraC11addDelegateyyAA0bcE0_pF">MapCamera.addDelegate(...)</a></code>. Query the bounding box of the
camera viewport using <code><a href="Classes/MapCamera.html#/s:7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp">MapCamera.boundingBox</a></code> (it may be extended)
and then use the method <code>GeoBox.contains(GeoCoordinates)</code> in combination with
<code><a href="Classes/MapCamera/State.html#/s:7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">MapCamera.State.distanceToTargetInMeters</a></code> to determine which MapMarkers are actually visible
to the user in the current camera viewport and thus need to be added to the map.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapmarker">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapMarker</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapMarker3DC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapMarker3D"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC">MapMarker3D</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a 3D shape drawn on the map at specified geodetic coordinates.</p>
<p>It can have a solid color or be textured, depending on the data from
<code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker3dmodel">MapMarker3DModel</a></code>.</p>
<p>By default, a 3D marker is drawn on top of all map content, including
3D map elements like extruded buildings or 3D landmarks. This can be
changed by enabling depth check using <code><a href="Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC19isDepthCheckEnabledSbvp">MapMarker3D.isDepthCheckEnabled</a></code>.</p>
<p>The display of a 3D marker is only guaranteed in case its origin is within
the viewport. At the moment, this is a known limitation that mostly affects
a 3D marker that is visually large and covers a sizeable part of the viewport.</p>
<h1 class="heading" id="sizing-and-scaling">Sizing and scaling</h1>
<p>Two aspects determine how big the <code>MapMarker3D</code> will be on the screen
and how will it behave when the map is zoomed in and out.</p>
<p>The first, and most impactful is <code><a href="sdk-for-ios-explore-api-reference-structs-rendersize-unit">RenderSize.Unit</a></code>, which specifies
how the vertex coordinates of the 3D model are interpreted.
Most importantly, it specifies whether the 3D model is placed
in world or screen coordinate space.</p>
<p><code><a href="Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">RenderSize.Unit.meters</a></code> will make the 3D model use world
coordinate space, meaning that it will change size together with the map
when it is zoomed in and out.</p>
<p><code><a href="Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> makes the 3D model use screen coordinate space,
meaning that it will have constant size on the screen regardless
of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle
will have a size of 10 by 10 pixels on the screen.</p>
<p><code><a href="Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO24densityIndependentPixelsyA2EmF">RenderSize.Unit.densityIndependentPixels</a></code> is similar to pixels,
but the resulting size will take into account the pixel density of the
display, meaning that physical size on the screen will be approximately
the same regardless of the size or resolution of the display.</p>
<p>The second aspect that determines size of <code>MapMarker3D</code> is scale.
It can be specified at construction time and can be changed later
at any time using <code><a href="Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC5scaleSdvp">MapMarker3D.scale</a></code>.</p>
<h1 class="heading" id="modifying-at-runtime">Modifying at runtime</h1>
<p>A 3D marker can be moved around a map by updating its coordinates using
<code><a href="Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC11coordinatesAA14GeoCoordinatesVvp">MapMarker3D.coordinates</a></code>.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker’s elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
<p>Its orientation is specified by bearing, pitch and roll and can be changed
by using <code><a href="Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC7bearingSdvp">MapMarker3D.bearing</a></code>, <code><a href="Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC5pitchSdvp">MapMarker3D.pitch</a></code>
and <code><a href="Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC4rollSdvp">MapMarker3D.roll</a></code>.</p>
<h1 class="heading" id="flat-marker">Flat marker</h1>
<p>A flat marker is a special case of a 3D marker, where the 3D shape being drawn
is a simple textured rectangle. In essence it’s an image drawn “on the ground”.
Such 3D marker can be conveniently created using
<code>MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit)</code>
constructor. Of course, once created, it can be rotated to face any direction.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapmarker3d">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapMarker3D</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker3D</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker3D</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarker3DModelC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapMarker3DModel"></a>
<a class="token" href="#/s:7heresdk16MapMarker3DModelC">MapMarker3DModel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a 3D model that can be used by a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker3d">MapMarker3D</a></code> to be shown on the map.
Geometry of 3D marker can be provided in form of a Wavefront OBJ file as specified in
<a href="http://www.martinreddy.net/gfx/3d/OBJ.spec">http://www.martinreddy.net/gfx/3d/OBJ.spec</a> or as mesh built via <code><a href="sdk-for-ios-explore-api-reference-classes-meshbuilder">MeshBuilder</a></code>.</p>
<h1 class="heading" id="1-creating-code-mapmarker3dmodel-code-from-obj-file">1. Creating <code>MapMarker3DModel</code> from OBJ file</h1>
<p>For OBJ files, HERE SDK only supports the following set of features of the OBJ specification:</p>
<ul>
<li>Triangle Meshes</li>
<li>Following vertex attributes must be present:

<ul>
<li>Vertex Position</li>
<li>Vertex Normal</li>
<li>Texture Coordinates</li>
<li>Geometry must be indexed (contain an Index Buffer)</li>
<li>Face element</li>
</ul></li>
</ul>
<p>HERE SDK does not support:</p>
<ul>
<li>Multi Texturing</li>
<li>Materials (mtllib [external .mtl file name] )

<ul>
<li>Lines</li>
<li>Higher Order Surfaces</li>
<li>Vendor specific extensions</li>
</ul></li>
</ul>
<p>For supported texture formats, HERE SDK allows the following formats to be specified:
JPG, PNG, GPU compressed texture formats: ECT1 (OpenGL only), YUV, ASTC, KTX.</p>
<h1 class="heading" id="2-creating-code-mapmarker3dmodel-code-programatically">2. Creating <code>MapMarker3DModel</code> programatically</h1>
<p>A 3D mesh can be specified programatically using <code><a href="sdk-for-ios-explore-api-reference-classes-meshbuilder">MeshBuilder</a></code> and passed to
<code>MapMarker3DModel</code> constructor. This method supports creating a mesh from
quads and triangles. Textured geometry is also supported, the mesh faces
need to have texture coordinates and a texture file needs to be passed
along with the mesh to <code>MapMarker3DModel</code> constructor.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapmarker3dmodel">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapMarker3DModel</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker3DModel</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker3DModel</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMarkerAnimationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapMarkerAnimation"></a>
<a class="token" href="#/s:7heresdk18MapMarkerAnimationC">MapMarkerAnimation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An animation that can be applied to the <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code> object.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapmarkeranimation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapMarkerAnimation</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarkerAnimation</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarkerAnimation</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapMeasureV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MapMeasure"></a>
<a class="token" href="#/s:7heresdk10MapMeasureV">MapMeasure</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A map measure.
Check <code><a href="sdk-for-ios-explore-api-reference-classes-mapcamera">MapCamera</a></code> for more details on each supported measure.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-mapmeasure">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapMeasure</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29MapMeasureDependentRenderSizeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MapMeasureDependentRenderSize"></a>
<a class="token" href="#/s:7heresdk29MapMeasureDependentRenderSizeV">MapMeasureDependentRenderSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a render size, described as map measure dependent values.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-mapmeasuredependentrendersize">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapMeasureDependentRenderSize</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapPolygonC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapPolygon"></a>
<a class="token" href="#/s:7heresdk10MapPolygonC">MapPolygon</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A visual representation of a polygon on the map. Can be used to visualize areas of all shapes
and sizes.</p>
<p>The geometry to be visualized is represented by an instance of <code><a href="sdk-for-ios-explore-api-reference-structs-geopolygon">GeoPolygon</a></code>.
To display circular areas (for example, a position accuracy indicator) use a GeoPolygon
created from a <code><a href="sdk-for-ios-explore-api-reference-structs-geocircle">GeoCircle</a></code> using <code>GeoPolygon.init(GeoCircle)</code>.</p>
<p>Note:</p>
<ul>
<li>The polygon shape should not cover more than half of the globe,
otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mappolygon">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapPolygon</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolygon</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolygon</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapPolyline"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC">MapPolyline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A visual representation of a line on the map.</p>
<p>The geometry to be visualized is represented by an instance of <code><a href="sdk-for-ios-explore-api-reference-structs-geopolyline">GeoPolyline</a></code>.</p>
<p>Altitude component of <code><a href="sdk-for-ios-explore-api-reference-structs-geopolyline">GeoPolyline</a></code>‘s vertices is ignored.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mappolyline">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapPolyline</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolyline</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolyline</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MapPolylineAnimationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapPolylineAnimation"></a>
<a class="token" href="#/s:7heresdk20MapPolylineAnimationC">MapPolylineAnimation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An animation that can be applied to the <code><a href="sdk-for-ios-explore-api-reference-classes-mappolyline">MapPolyline</a></code> object.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mappolylineanimation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapPolylineAnimation</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolylineAnimation</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolylineAnimation</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapPickResultC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapPickResult"></a>
<a class="token" href="#/s:7heresdk13MapPickResultC">MapPickResult</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A class representing a map pick result.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mappickresult">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapPickResult</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPickResult</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPickResult</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapSceneC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapScene"></a>
<a class="token" href="#/s:7heresdk8MapSceneC">MapScene</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a map scene and exposes the functionality to manipulate its content.</p>
<h2 class="heading" id="map-schemes">Map schemes</h2>
<p>The content of the displayed map and how it looks is specified by a
<code><a href="sdk-for-ios-explore-api-reference-enums-mapscheme">MapScheme</a></code> which is set when loading a scene with <code>MapScene.loadScene(MapScheme, MapScene.LoadSceneCompletionHandler?)</code>.
It is also possible to load your own custom map scheme from a file bundled
with your application. Supported file formats are:</p>
<ul>
<li>JSON (file extension ‘.json’; e.g. ‘my_custom_style.json’)</li>
<li>ZIP archive (file extension ‘.zip’; e.g. ‘my_custom_style.zip’), with the following archive structure:

<ul>
<li>root folder: any, not empty (e.g. ‘my_custom_style’)</li>
<li>JSON configuration: ‘<root folder="">/style.json’</root></li>
<li>custom assets folder: ‘<root folder="">/assets’</root></li>
</ul></li>
</ul>
<h2 class="heading" id="map-features">Map features</h2>
<p>Different map schemes offer different sets of features, for example showing traffic or 3D buildings.
Some features have multiple modes of operation, but most have only one.
<code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC20getSupportedFeaturesSDySSSaySSGGyF">MapScene.getSupportedFeatures(...)</a></code> can be used to check what features and modes are supported
for the current scene. Features can be enabled using <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> and disabled
with <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC15disableFeaturesyySaySSGF">MapScene.disableFeatures(...)</a></code>. Checking which features are currently enabled can be done using
<code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF">MapScene.getActiveFeatures(...)</a></code>. For convenience, <code><a href="sdk-for-ios-explore-api-reference-structs-mapfeatures">MapFeatures</a></code> and <code><a href="sdk-for-ios-explore-api-reference-structs-mapfeaturemodes">MapFeatureModes</a></code> hold
constants for feature and mode names.</p>
<p>Since version 4.15.0, map features cannot be controlled using <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">MapScene.setLayerVisibility(...)</a></code>, since <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">MapScene.setLayerVisibility(...)</a></code> controls
only visibility of the layers which are corresponding to the features enabled either by <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code>
or enabled by default for the scene.</p>
<h2 class="heading" id="map-layers">Map layers</h2>
<p>A map scheme is organized in layers, which can be controlled using <code><a href="Classes/MapScene.html#/s:7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">MapScene.setLayerVisibility(...)</a></code>.
It’s possible to change the visibility state of any map layer as long as the name is known.</p>
<p>Layer visibility settings persist between scene reloading.</p>
<h2 class="heading" id="user-content">User content</h2>
<p>User generated content can be visualised on the map using <code><a href="sdk-for-ios-explore-api-reference-classes-mappolyline">MapPolyline</a></code>, <code><a href="sdk-for-ios-explore-api-reference-classes-mappolygon">MapPolygon</a></code>, <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code>,
<code><a href="sdk-for-ios-explore-api-reference-classes-mapmarkercluster">MapMarkerCluster</a></code>, <code><a href="sdk-for-ios-explore-api-reference-classes-maparrow">MapArrow</a></code>, <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker3d">MapMarker3D</a></code> and <code><a href="sdk-for-ios-explore-api-reference-classes-mapimageoverlay">MapImageOverlay</a></code>
(collectively referred to as “map items”). Those can be added to and removed
from the scene by respective add and remove methods. The render order of the map items
is according to the list above. The order of objects within the same type can be controlled using
the <code>drawOrder</code> property of each object.</p>
<p>Be careful when adding a very large number of map items as this can have a negative impact on
the performance of the app.
To work around this limitation the following approach can be used:
Register to map camera updates using <code><a href="Classes/MapCamera.html#/s:7heresdk9MapCameraC11addDelegateyyAA0bcE0_pF">MapCamera.addDelegate(...)</a></code>. Query the bounding box of the
camera viewport using <code><a href="Classes/MapCamera.html#/s:7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp">MapCamera.boundingBox</a></code> (it may be extended) and then use the method
<code>GeoBox.contains(GeoCoordinates)</code> in combination with <code><a href="Classes/MapCamera/State.html#/s:7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">MapCamera.State.distanceToTargetInMeters</a></code> to
determine which map items are actually visible to the user in the current camera viewport and
thus need to be added to the map.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapscene">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapScene</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapScene</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapScene</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapSchemeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MapScheme"></a>
<a class="token" href="#/s:7heresdk9MapSchemeO">MapScheme</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the preconfigured map schemes bundled with the SDK.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-mapscheme">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MapScheme</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/MapViewBase"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP">MapViewBase</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the available public API from  <code><a href="sdk-for-ios-explore-api-reference-classes-mapview">MapView</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-mapviewbase">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">MapViewBase</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/c:@M@heresdk@objc(cs)HereMapView"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapView"></a>
<a class="token" href="#/c:@M@heresdk@objc(cs)HereMapView">MapView</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A view that displays a map.
Note: Before using this class, <code><a href="sdk-for-ios-explore-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> must be already initialized.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapview">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@IBDesignable</span>
<span class="kd">@objc(HereMapView)</span>
<span class="kd">@MainActor</span>
<span class="kd">open</span> <span class="kd">class</span> <span class="kt">MapView</span> <span class="p">:</span> <span class="kt">UIView</span><span class="p">,</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-mapviewbase">MapViewBase</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24MapViewLifecycleDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/MapViewLifecycleDelegate"></a>
<a class="token" href="#/s:7heresdk24MapViewLifecycleDelegateP">MapViewLifecycleDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides a mechanism for observing a lifecycle of a map view and/or implementing components
whose lifecycle needs to be linked with that of a map view.</p>
<p>Storing the map view in a strong reference is strongly discouraged, as that
will create a reference cycle and prevent map view from being released.</p>
<p>A <code><a href="sdk-for-ios-explore-api-reference-classes-mapview">MapView</a></code> is using a
<a href="https://developer.apple.com/documentation/quartzcore/cametallayer">CAMetalLayer</a></p>
<p>to render its content.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-mapviewlifecycledelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">MapViewLifecycleDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapViewOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MapViewOptions"></a>
<a class="token" href="#/s:7heresdk14MapViewOptionsV">MapViewOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options used for initialization of map view</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-mapviewoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapViewOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MaterialReflectivityV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MaterialReflectivity"></a>
<a class="token" href="#/s:7heresdk20MaterialReflectivityV">MaterialReflectivity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Material reflectivity properties are used to enable per‑pixel lighting for supported map objects
(e.g. <code><a href="sdk-for-ios-explore-api-reference-classes-locationindicator">LocationIndicator</a></code> markers and their halo).</p>
<h2 class="heading" id="lighting-off-vs-on">Lighting OFF vs ON</h2>
<p>By default (when no MaterialReflectivity is assigned) objects are rendered “unlit” (emissive):
their texture / color appears at a constant brightness, unaffected by scene lights. Assigning a
<code>MaterialReflectivity</code> instance to an object that supports it (e.g. <code><a href="Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC20materialReflectivityAA08MaterialE0VSgvp">LocationIndicator.materialReflectivity</a></code>)
automatically enables lighting for this object and all its internal components. Clearing (setting the property to
<code>nil</code>) disables lighting again and restores the unlit appearance.</p>
<h2 class="heading" id="factors">Factors</h2>
<p>Both factors are expected to be within [0.0, 1.0]. Values outside this range are allowed but may
produce exaggerated results or be clamped by future implementations. Typical useful ranges:</p>
<ul>
<li>ambientFactor: 0.0 – 0.4 (higher values flatten the shading and reduce directional contrast)</li>
<li>diffuseFactor: 0.5 – 1.0 (lower values dim the object under directional light)</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-materialreflectivity">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MaterialReflectivity</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4MeshC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Mesh"></a>
<a class="token" href="#/s:7heresdk4MeshC">Mesh</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a mesh in 3D space. Such meshes are built using <code><a href="sdk-for-ios-explore-api-reference-classes-meshbuilder">MeshBuilder</a></code>.</p>
<p>The class is not offering any methods, as its data is only meant to be consumed internally
when being passed to <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker3dmodel">MapMarker3DModel</a></code> constructor.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Mesh</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Mesh</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Mesh</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MeshBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MeshBuilder"></a>
<a class="token" href="#/s:7heresdk11MeshBuilderC">MeshBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder for meshes. Such meshes can contain different kinds of primitives, like quads or
triangles. Both primitives support adding texture coordinates that are mapped to the
corners of the primitives. See <code><a href="sdk-for-ios-explore-api-reference-classes-trianglemeshbuilder">TriangleMeshBuilder</a></code> and <code><a href="sdk-for-ios-explore-api-reference-classes-quadmeshbuilder">QuadMeshBuilder</a></code> for more details.</p>
<p>Note: Normals cannot be set as they are not necessary when using the <code>MeshBuilder</code>.</p>
<p><strong>Example how to build a cube using <code><a href="sdk-for-ios-explore-api-reference-classes-quadmeshbuilder">QuadMeshBuilder</a></code></strong></p>
<pre class="highlight swift"><code><span class="k">let</span> <span class="nv">cube</span> <span class="o">=</span> <span class="kt">MeshBuilder</span><span class="p">()</span>
    <span class="o">.</span><span class="nf">quad</span><span class="p">(</span><span class="nv">a</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">b</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">c</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">d</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">))</span>
    <span class="o">.</span><span class="nf">quad</span><span class="p">(</span><span class="nv">a</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">b</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">c</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">d</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">))</span>
    <span class="o">.</span><span class="nf">quad</span><span class="p">(</span><span class="nv">a</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">b</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">c</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">d</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">))</span>
    <span class="o">.</span><span class="nf">quad</span><span class="p">(</span><span class="nv">a</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">b</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">c</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">d</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">))</span>
    <span class="o">.</span><span class="nf">quad</span><span class="p">(</span><span class="nv">a</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">b</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">c</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">d</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">))</span>
    <span class="o">.</span><span class="nf">quad</span><span class="p">(</span><span class="nv">a</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">b</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">c</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">),</span>
          <span class="nv">d</span><span class="p">:</span> <span class="kt">Point3D</span><span class="p">(</span><span class="nv">x</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">y</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">,</span> <span class="nv">z</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.5</span><span class="p">))</span>
    <span class="o">.</span><span class="nf">build</span><span class="p">()</span>
</code></pre>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-meshbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MeshBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MeshBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MeshBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PanDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/PanDelegate"></a>
<a class="token" href="#/s:7heresdk11PanDelegateP">PanDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol for handling pan gestures.
Pan gesture occurs when a finger is moving on the screen.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-pandelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">PanDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20PickMapContentResultC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PickMapContentResult"></a>
<a class="token" href="#/s:7heresdk20PickMapContentResultC">PickMapContentResult</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A class that contains possible results from picking map content on the map scene.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-pickmapcontentresult">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PickMapContentResult</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PickMapContentResult</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PickMapContentResult</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PickMapItemsResultC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PickMapItemsResult"></a>
<a class="token" href="#/s:7heresdk18PickMapItemsResultC">PickMapItemsResult</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Carries results from the picking of map items on the map scene.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-pickmapitemsresult">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PickMapItemsResult</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PickMapItemsResult</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PickMapItemsResult</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PinchRotateDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/PinchRotateDelegate"></a>
<a class="token" href="#/s:7heresdk19PinchRotateDelegateP">PinchRotateDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol for handling pinch rotate gestures.
Pinch rotate gesture occurs when two fingers are on the screen
and at least one of them moves.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-pinchrotatedelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">PinchRotateDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9PointDataC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PointData"></a>
<a class="token" href="#/s:7heresdk9PointDataC">PointData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a geodetic point with custom attributes.
Can be created using a <code><a href="sdk-for-ios-explore-api-reference-classes-pointdatabuilder">PointDataBuilder</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PointData</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointData</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointData</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PointDataAccessorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PointDataAccessor"></a>
<a class="token" href="#/s:7heresdk17PointDataAccessorC">PointDataAccessor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Point data accessor used for manipulating points that are part of a PointDataSource.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-pointdataaccessor">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PointDataAccessor</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataAccessor</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataAccessor</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16PointDataBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PointDataBuilder"></a>
<a class="token" href="#/s:7heresdk16PointDataBuilderC">PointDataBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder of <code><a href="Maps.html#/s:7heresdk9PointDataC">PointData</a></code> instances.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-pointdatabuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PointDataBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15PointDataSourceC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PointDataSource"></a>
<a class="token" href="#/s:7heresdk15PointDataSourceC">PointDataSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Point data source allows the rendering engine access to the user provided
geographical locations and their attributes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-pointdatasource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PointDataSource</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataSource</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataSource</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22PointDataSourceBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PointDataSourceBuilder"></a>
<a class="token" href="#/s:7heresdk22PointDataSourceBuilderC">PointDataSourceBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder of points data source.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-pointdatasourcebuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PointDataSourceBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataSourceBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataSourceBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PointTileDataSourceC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PointTileDataSource"></a>
<a class="token" href="#/s:7heresdk19PointTileDataSourceC">PointTileDataSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Point tile data source allows the rendering engine access to user managed data sets of
geographical locations and their attributes through a <code><a href="sdk-for-ios-explore-api-reference-protocols-pointtilesource">PointTileSource</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-pointtiledatasource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PointTileDataSource</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointTileDataSource</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointTileDataSource</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15PointTileSourceP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/PointTileSource"></a>
<a class="token" href="#/s:7heresdk15PointTileSourceP">PointTileSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A source of geodetic point tiles.
The implementations must be thread-safe.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-pointtilesource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">PointTileSource</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-tilesource">TileSource</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32PointTileSourceLoadResultHandlerP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/PointTileSourceLoadResultHandler"></a>
<a class="token" href="#/s:7heresdk32PointTileSourceLoadResultHandlerP">PointTileSourceLoadResultHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Result handler of a load tile request.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-pointtilesourceloadresulthandler">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">PointTileSourceLoadResultHandler</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15Point2DKeyframeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Point2DKeyframe"></a>
<a class="token" href="#/s:7heresdk15Point2DKeyframeV">Point2DKeyframe</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A Point2D keyframe. A keyframe consists of a value and an animation duration.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-point2dkeyframe">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Point2DKeyframe</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PolygonDataC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PolygonData"></a>
<a class="token" href="#/s:7heresdk11PolygonDataC">PolygonData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a geodetic polygon with custom attributes.
Can be created using a <code><a href="sdk-for-ios-explore-api-reference-classes-polygondatabuilder">PolygonDataBuilder</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PolygonData</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonData</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonData</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PolygonDataAccessorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PolygonDataAccessor"></a>
<a class="token" href="#/s:7heresdk19PolygonDataAccessorC">PolygonDataAccessor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-polygondataaccessor">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PolygonDataAccessor</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataAccessor</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataAccessor</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PolygonDataBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PolygonDataBuilder"></a>
<a class="token" href="#/s:7heresdk18PolygonDataBuilderC">PolygonDataBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder of <code><a href="Maps.html#/s:7heresdk11PolygonDataC">PolygonData</a></code> instances.</p>
<p>The builder can create <code><a href="Maps.html#/s:7heresdk11PolygonDataC">PolygonData</a></code> instances for polygons with an outer boundary and
optionally one or more inner boundaries (holes).</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-polygondatabuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PolygonDataBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PolygonDataSourceC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PolygonDataSource"></a>
<a class="token" href="#/s:7heresdk17PolygonDataSourceC">PolygonDataSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Polygon data source allows the rendering engine access to the user provided
polygons geometry and their attributes.</p>
<p>Polygon segments are rendered following the shortest path between their end points.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-polygondatasource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PolygonDataSource</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataSource</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataSource</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PolygonDataSourceBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PolygonDataSourceBuilder"></a>
<a class="token" href="#/s:7heresdk24PolygonDataSourceBuilderC">PolygonDataSourceBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder of the polygons data source.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-polygondatasourcebuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PolygonDataSourceBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataSourceBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonDataSourceBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21PolygonTileDataSourceC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PolygonTileDataSource"></a>
<a class="token" href="#/s:7heresdk21PolygonTileDataSourceC">PolygonTileDataSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Polygon tile data source allows the rendering engine access to user managed data sets of
geodetic polygons and their attributes through a <code><a href="sdk-for-ios-explore-api-reference-protocols-polygontilesource">PolygonTileSource</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-polygontiledatasource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PolygonTileDataSource</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonTileDataSource</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolygonTileDataSource</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PolygonTileSourceP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/PolygonTileSource"></a>
<a class="token" href="#/s:7heresdk17PolygonTileSourceP">PolygonTileSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A source of geodetic polygon tiles.
Polygons provided by an implementation must be clipped to the boundaries of the requested tile.
The implementations must be thread-safe.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-polygontilesource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">PolygonTileSource</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-tilesource">TileSource</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk34PolygonTileSourceLoadResultHandlerP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/PolygonTileSourceLoadResultHandler"></a>
<a class="token" href="#/s:7heresdk34PolygonTileSourceLoadResultHandlerP">PolygonTileSourceLoadResultHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Result handler of a load tile request.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-polygontilesourceloadresulthandler">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">PolygonTileSourceLoadResultHandler</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15QuadMeshBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/QuadMeshBuilder"></a>
<a class="token" href="#/s:7heresdk15QuadMeshBuilderC">QuadMeshBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder for a single quad.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-quadmeshbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">QuadMeshBuilder</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-meshbuilder">MeshBuilder</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RasterDataSourceC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/RasterDataSource"></a>
<a class="token" href="#/s:7heresdk16RasterDataSourceC">RasterDataSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Data source to load map layers using a raster image format (jpg, png).
The example below illustrates how to create a raster data source and how to link it to
a newly created map layer.</p>
<pre class="highlight swift"><code>  <span class="k">let</span> <span class="nv">rasterDataSource</span> <span class="o">=</span> <span class="kt">RasterDataSource</span><span class="p">(</span><span class="n">mapContext</span><span class="p">,</span> <span class="n">rasterDataSourceConfig</span><span class="p">)</span>

  <span class="k">let</span> <span class="nv">layer</span> <span class="o">=</span> <span class="kt">MapLayerBuilder</span><span class="p">()</span>
     <span class="c1">// The name and the type of the data source have to be provided.</span>
     <span class="c1">// In our case, the name of the raster data source is in rasterDataSourceConfig.</span>
     <span class="o">.</span><span class="nf">withDataSource</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="n">rasterDataSourceConfig</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="nv">contentType</span><span class="p">:</span> <span class="kt">MapContentType</span><span class="o">.</span><span class="n">rasterImage</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">forMap</span><span class="p">(</span><span class="n">map</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withName</span><span class="p">(</span><span class="s">"rasterLayer"</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">();</span>
</code></pre>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-rasterdatasource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">RasterDataSource</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RasterDataSource</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RasterDataSource</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29RasterDataSourceConfigurationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RasterDataSourceConfiguration"></a>
<a class="token" href="#/s:7heresdk29RasterDataSourceConfigurationV">RasterDataSourceConfiguration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called on the main thread after <code>fromJsonFile()</code> method finishes loading
the configuration.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-rasterdatasourceconfiguration">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RasterDataSourceConfiguration</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk35RasterDataSourceConfigurationUpdateV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RasterDataSourceConfigurationUpdate"></a>
<a class="token" href="#/s:7heresdk35RasterDataSourceConfigurationUpdateV">RasterDataSourceConfigurationUpdate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configuration update for a RasterDataSource.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-rasterdatasourceconfigurationupdate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RasterDataSourceConfigurationUpdate</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RasterDataSourceDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/RasterDataSourceDelegate"></a>
<a class="token" href="#/s:7heresdk24RasterDataSourceDelegateP">RasterDataSourceDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Delegate for RasterDataSource events.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-rasterdatasourcedelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">RasterDataSourceDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21RasterDataSourceErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RasterDataSourceError"></a>
<a class="token" href="#/s:7heresdk21RasterDataSourceErrorO">RasterDataSourceError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Raster data source error codes.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-rasterdatasourceerror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RasterDataSourceError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RasterTileSourceP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/RasterTileSource"></a>
<a class="token" href="#/s:7heresdk16RasterTileSourceP">RasterTileSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A source of raster tiles.
The implementations must be thread-safe.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-rastertilesource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">RasterTileSource</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-tilesource">TileSource</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33RasterTileSourceLoadResultHandlerP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/RasterTileSourceLoadResultHandler"></a>
<a class="token" href="#/s:7heresdk33RasterTileSourceLoadResultHandlerP">RasterTileSourceLoadResultHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Result handler of a load tile request.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-rastertilesourceloadresulthandler">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">RasterTileSourceLoadResultHandler</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RoadShieldIconPropertiesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadShieldIconProperties"></a>
<a class="token" href="#/s:7heresdk24RoadShieldIconPropertiesV">RoadShieldIconProperties</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains the information required to create a road shield image.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-roadshieldiconproperties">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadShieldIconProperties</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RenderSizeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RenderSize"></a>
<a class="token" href="#/s:7heresdk10RenderSizeV">RenderSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents size of visual elements drawn on the map.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-rendersize">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RenderSize</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ScalarKeyframeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ScalarKeyframe"></a>
<a class="token" href="#/s:7heresdk14ScalarKeyframeV">ScalarKeyframe</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A ScalarKeyframe consists of a scalar value (e.g,: distance in meters) and an animation duration.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-scalarkeyframe">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ScalarKeyframe</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/c:@M@heresdk@objc(cs)SDKMapViewInitializer"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SDKMapViewInitializer"></a>
<a class="token" href="#/c:@M@heresdk@objc(cs)SDKMapViewInitializer">SDKMapViewInitializer</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Do not use this. This class is used to initialize internals of the SDK.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-sdkmapviewinitializer">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SDKMapViewInitializer</span> <span class="p">:</span> <span class="kt">NSObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13ShadowQualityO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ShadowQuality"></a>
<a class="token" href="#/s:7heresdk13ShadowQualityO">ShadowQuality</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The shadow quality. Controls the quality of the shadow cascade (i.e. the size of the shadow
maps and the cascade count), which is shared by all views.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-shadowquality">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ShadowQuality</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5StyleC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Style"></a>
<a class="token" href="#/s:7heresdk5StyleC">Style</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A style that defines the visual appearance of map rendered features.
A <code>Style</code> can be created using a <code><a href="sdk-for-ios-explore-api-reference-classes-jsonstylefactory">JsonStyleFactory</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-style">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Style</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Style</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Style</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TapDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TapDelegate"></a>
<a class="token" href="#/s:7heresdk11TapDelegateP">TapDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol for handling tap gestures.
Tap gesture occurs after tapping on the screen.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-tapdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TapDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TileGeoBoundsCalculatorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TileGeoBoundsCalculator"></a>
<a class="token" href="#/s:7heresdk23TileGeoBoundsCalculatorC">TileGeoBoundsCalculator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A calculator of geodetic bounds for tiles identified by keys generated
in a particular tiling scheme (<code><a href="sdk-for-ios-explore-api-reference-enums-tilingscheme">TilingScheme</a></code>).</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-tilegeoboundscalculator">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TileGeoBoundsCalculator</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TileGeoBoundsCalculator</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TileGeoBoundsCalculator</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10TileSourceP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TileSource"></a>
<a class="token" href="#/s:7heresdk10TileSourceP">TileSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A source of tiles.
The implementations must be thread-safe.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-tilesource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TileSource</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TileSourceDataVersionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TileSourceDataVersion"></a>
<a class="token" href="#/s:7heresdk21TileSourceDataVersionV">TileSourceDataVersion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tile data version.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-tilesourcedataversion">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TileSourceDataVersion</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18TileSourceDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TileSourceDelegate"></a>
<a class="token" href="#/s:7heresdk18TileSourceDelegateP">TileSourceDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Delegate for <code><a href="sdk-for-ios-explore-api-reference-protocols-tilesource">TileSource</a></code> events.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-tilesourcedelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TileSourceDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk014TileSourceLoadB13RequestHandleP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TileSourceLoadTileRequestHandle"></a>
<a class="token" href="#/s:7heresdk014TileSourceLoadB13RequestHandleP">TileSourceLoadTileRequestHandle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Handle of a load request.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-tilesourceloadtilerequesthandle">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TileSourceLoadTileRequestHandle</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk010TileSourceB8MetadataV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TileSourceTileMetadata"></a>
<a class="token" href="#/s:7heresdk010TileSourceB8MetadataV">TileSourceTileMetadata</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tile metadata.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-tilesourcetilemetadata">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TileSourceTileMetadata</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TileKeyV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TileKey"></a>
<a class="token" href="#/s:7heresdk7TileKeyV">TileKey</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Key of a data source tile.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-tilekey">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TileKey</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TileUrlProviderFactoryC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TileUrlProviderFactory"></a>
<a class="token" href="#/s:7heresdk22TileUrlProviderFactoryC">TileUrlProviderFactory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Factory for generating a <code><a href="Maps.html#/s:7heresdk21TileUrlRequestHandlera">TileUrlRequestHandler</a></code> utilized in creating a tile URL.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-tileurlproviderfactory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TileUrlProviderFactory</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TileUrlProviderFactory</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TileUrlProviderFactory</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TileUrlRequestHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/TileUrlRequestHandler"></a>
<a class="token" href="#/s:7heresdk21TileUrlRequestHandlera">TileUrlRequestHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides the URL as String for the given tile coordinates and storage level.</p>
<p>The first and second parameters correspond to the X and Y coordinates of the tile, respectively, and have values ranging from 0 to 2^level − 1.
The third parameter indicates the level of the tile.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">TileUrlRequestHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">x</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="n">_</span> <span class="nv">y</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="n">_</span> <span class="nv">level</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">String</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>x</em>
</code>
</td>
<td>
<div>
<p>X coordinate of the tile. This ranges from 0 to 2^level − 1.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>y</em>
</code>
</td>
<td>
<div>
<p>Y coordinate of the tile. This ranges from 0 to 2^level − 1.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>level</em>
</code>
</td>
<td>
<div>
<p>Level of the tile.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>the URL.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TilingSchemeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TilingScheme"></a>
<a class="token" href="#/s:7heresdk12TilingSchemeO">TilingScheme</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of available data tiling schemes.
X axis has the origin at -180 longitude and is increasing in east direction.
Y axis has the origin at max latitude and is increasing in south direction.
For half quad tree schemes, only the uppper half of the tree is used.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-tilingscheme">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TilingScheme</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24TranslucentMapLayerGroupC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TranslucentMapLayerGroup"></a>
<a class="token" href="#/s:7heresdk24TranslucentMapLayerGroupC">TranslucentMapLayerGroup</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A translucent layer group that can be the target for <code><a href="Classes/MapLayerPriorityBuilder.html#/s:7heresdk23MapLayerPriorityBuilderC7inGroupyACSSF">MapLayerPriorityBuilder.inGroup(...)</a></code>.
Currently, only custom line layers can be added to a translucent layer group.
Custom line layers in a translucent layer group are rendered in an offscreen translucent pass so
that overlapping translucent line geometry is not alpha blended with itself.
At creation, the layer group gets added to a map. The layer group gets removed from the map upon
instance destruction and any layer (categories) still in the group are not rendered anymore,
therefore it is recommended to keep a group alive as long as layers using the group are alive and
in use.</p>
<p>Conceptual example to place line layers into a translucent group:</p>
<pre class="highlight swift"><code> <span class="c1">// Create a translucent group with a unique name and a render priority</span>
 <span class="k">let</span> <span class="nv">groupPriority</span> <span class="o">=</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">()</span><span class="o">.</span><span class="nf">renderedLast</span><span class="p">()</span><span class="o">.</span><span class="nf">build</span><span class="p">()</span>
 <span class="k">let</span> <span class="nv">group</span> <span class="o">=</span> <span class="kt">TranslucentMapLayerGroup</span><span class="p">(</span><span class="nv">name</span><span class="p">:</span> <span class="s">"TranslucentGroupName"</span><span class="p">,</span> <span class="n">map</span><span class="p">,</span> <span class="n">groupPriority</span><span class="p">)</span>

 <span class="c1">// Create a line layer to be rendered as part of the translucent group</span>
 <span class="k">let</span> <span class="nv">lineLayerPriority</span> <span class="o">=</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">inGroup</span><span class="p">(</span><span class="s">"TranslucentGroupName"</span><span class="p">)</span> <span class="c1">// places the line layer into the group</span>
     <span class="o">.</span><span class="nf">renderedFirst</span><span class="p">()</span>                 <span class="c1">// to be rendered first when the group is rendered</span>
     <span class="o">.</span><span class="nf">withCategory</span><span class="p">(</span><span class="s">"SomeCategory"</span><span class="p">)</span>    <span class="c1">// places the line layer category 'SomeCategory'</span>
     <span class="o">.</span><span class="nf">inGroup</span><span class="p">(</span><span class="s">"TranslucentGroupName"</span><span class="p">)</span> <span class="c1">// into the group</span>
     <span class="o">.</span><span class="nf">renderedLast</span><span class="p">()</span>                  <span class="c1">// to be rendered last when the group is rendered</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">()</span>

 <span class="k">let</span> <span class="nv">lineLayer</span> <span class="o">=</span> <span class="kt">MapLayerBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">withDataSource</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"DataSourceName"</span><span class="p">,</span> <span class="nv">contentType</span><span class="p">:</span> <span class="kt">MapContentType</span><span class="o">.</span><span class="n">line</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">forMap</span><span class="p">(</span><span class="n">map</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withName</span><span class="p">(</span><span class="s">"LineLayerName"</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withPriority</span><span class="p">(</span><span class="n">lineLayerPriority</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withStyle</span><span class="p">(</span><span class="n">translucentLineStyle</span><span class="p">)</span> <span class="c1">// E.g. "technique": "line" ... "color": "#FFFFFF80"</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">()</span>

 <span class="c1">// Create a second line layer to be rendered as part of the translucent group</span>
 <span class="k">let</span> <span class="nv">secondLineLayerPriority</span> <span class="o">=</span> <span class="kt">MapLayerPriorityBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">inGroup</span><span class="p">(</span><span class="s">"TranslucentGroupName"</span><span class="p">)</span>      <span class="c1">// places the second line layer into the group</span>
     <span class="o">.</span><span class="nf">renderedBeforeLayer</span><span class="p">(</span><span class="s">"LineLayerName"</span><span class="p">)</span> <span class="c1">// to be rendered before first layer</span>
                                           <span class="c1">// when the group is rendered</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">()</span>

 <span class="k">let</span> <span class="nv">secondLineLayer</span> <span class="o">=</span> <span class="kt">MapLayerBuilder</span><span class="p">()</span>
     <span class="o">.</span><span class="nf">withDataSource</span><span class="p">(</span><span class="nv">named</span><span class="p">:</span> <span class="s">"SecondDataSourceName"</span><span class="p">,</span> <span class="nv">contentType</span><span class="p">:</span> <span class="kt">MapContentType</span><span class="o">.</span><span class="n">line</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">forMap</span><span class="p">(</span><span class="n">map</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withName</span><span class="p">(</span><span class="s">"SecondLineLayerName"</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withPriority</span><span class="p">(</span><span class="n">secondLineLayerPriority</span><span class="p">)</span>
     <span class="o">.</span><span class="nf">withStyle</span><span class="p">(</span><span class="n">secondTranslucentLineStyle</span><span class="p">)</span> <span class="c1">// E.g. "technique": "line" ... "color": "#FFFFFF80"</span>
     <span class="o">.</span><span class="nf">build</span><span class="p">()</span>
</code></pre>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-translucentmaplayergroup">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TranslucentMapLayerGroup</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TranslucentMapLayerGroup</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TranslucentMapLayerGroup</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TriangleMeshBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TriangleMeshBuilder"></a>
<a class="token" href="#/s:7heresdk19TriangleMeshBuilderC">TriangleMeshBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder for a single triangle.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-trianglemeshbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TriangleMeshBuilder</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-meshbuilder">MeshBuilder</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20TwoFingerPanDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TwoFingerPanDelegate"></a>
<a class="token" href="#/s:7heresdk20TwoFingerPanDelegateP">TwoFingerPanDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol for handling two finger pan gestures.
Two finger pan gesture occurs when two fingers are on the screen
and both of them are moving vertically.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-twofingerpandelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TwoFingerPanDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20TwoFingerTapDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TwoFingerTapDelegate"></a>
<a class="token" href="#/s:7heresdk20TwoFingerTapDelegateP">TwoFingerTapDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol for handling two finger tap gestures.
Two finger tap gesture occurs after tapping on the screen with two fingers.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-twofingertapdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TwoFingerTapDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisibilityStateO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/VisibilityState"></a>
<a class="token" href="#/s:7heresdk15VisibilityStateO">VisibilityState</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the visibility state of an SDK map view’s object.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-visibilitystate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">VisibilityState</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14WatermarkStyleO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/WatermarkStyle"></a>
<a class="token" href="#/s:7heresdk14WatermarkStyleO">WatermarkStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the style of the HERE watermark logo. The dark watermark should be used for custom
schemes that are brighter (like daytime) and the light watermark for darker custom schemes (like
night or satellite based).</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-watermarkstyle">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">WatermarkStyle</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
} </HTMLBlock>

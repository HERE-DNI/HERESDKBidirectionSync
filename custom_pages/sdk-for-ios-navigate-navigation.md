---
title: "Navigation"
slug: "sdk-for-ios-navigate-navigation"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/Navigation"></a>
<a title="Navigation  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

        Navigation  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Navigation</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AreaCameraBehaviorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/AreaCameraBehavior"></a>
<a class="token" href="#/s:7heresdk18AreaCameraBehaviorC">AreaCameraBehavior</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Use this class to show an overview of geo points. By default, the orientation of the camera will be
perpendicular to the Earth’s surface (ie. looking towards the center of the Earth),
while bearing will be towards north.</p>
<p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are
subject to change without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-areacamerabehavior">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">AreaCameraBehavior</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-camerabehavior">CameraBehavior</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AreaCameraBehavior</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AreaCameraBehavior</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25ArrivalNotificationOptionO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ArrivalNotificationOption"></a>
<a class="token" href="#/s:7heresdk25ArrivalNotificationOptionO">ArrivalNotificationOption</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates arrival point type to announce in maneuver notification.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-arrivalnotificationoption">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ArrivalNotificationOption</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11AspectRatioO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/AspectRatio"></a>
<a class="token" href="#/s:7heresdk11AspectRatioO">AspectRatio</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The aspect ratio of the image.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-aspectratio">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">AspectRatio</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AutomotiveCameraBehaviorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/AutomotiveCameraBehavior"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorC">AutomotiveCameraBehavior</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides a high-level camera controller for automotive navigation that manages both tracking
and area camera behaviors. This class acts as a facade, delegating camera operations to either
a <code><a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">TrackingCameraBehavior</a></code> for following the vehicle during navigation or an <code><a href="sdk-for-ios-navigate-classes-areacamerabehavior">AreaCameraBehavior</a></code>
for showing overview areas such as points of interest or route previews.</p>
<p>The controller supports three states: tracking mode (following the vehicle), area mode (showing
geographic regions), or inactive (no automatic camera control). The inactive state allows
external control of the camera, such as when responding to user touch events or when UI logic
temporarily disables automatic camera behavior.</p>
<p>Camera configuration, including animation durations, zoom policies, and maneuver handling
settings, can be provided through a JSON configuration string or file. The configuration is
validated and parsed during construction.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-automotivecamerabehavior">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">AutomotiveCameraBehavior</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-camerabehavior">CameraBehavior</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AutomotiveCameraBehavior</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AutomotiveCameraBehavior</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18BorderCrossingTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/BorderCrossingType"></a>
<a class="token" href="#/s:7heresdk18BorderCrossingTypeO">BorderCrossingType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of a border crossing given in a <code><a href="sdk-for-ios-navigate-structs-bordercrossingwarning">BorderCrossingWarning</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-bordercrossingtype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">BorderCrossingType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BorderCrossingWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/BorderCrossingWarning"></a>
<a class="token" href="#/s:7heresdk21BorderCrossingWarningV">BorderCrossingWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A border crossing. The main field describing the border crossing is <code><a href="Structs/BorderCrossingWarning.html#/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp">BorderCrossingWarning.type</a></code> specifying whether the border crossing
is given for a country border or a state border. The <code><a href="Structs/BorderCrossingWarning.html#/s:7heresdk21BorderCrossingWarningV4typeAA0bC4TypeOvp">BorderCrossingWarning.type</a></code> must be known.
The country and state codes are contained in <code><a href="Structs/BorderCrossingWarning.html#/s:7heresdk21BorderCrossingWarningV19administrativeRulesAA014AdministrativeF0Vvp">BorderCrossingWarning.administrativeRules</a></code> along with other information such as speed
limits, u-turn regulations or pre-trip planning information contained by the <code><a href="sdk-for-ios-navigate-structs-administrativerules">AdministrativeRules</a></code>.</p>
<p>Use <code>BorderCrossingWarningListener</code> to get notifications about upcoming country or state border crossings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-bordercrossingwarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BorderCrossingWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29BorderCrossingWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/BorderCrossingWarningDelegate"></a>
<a class="token" href="#/s:7heresdk29BorderCrossingWarningDelegateP">BorderCrossingWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol
should be implemented in order to receive border crossing warnings for country and state borders.
<strong>Note:</strong> The border crossing warner is a point warner, which means that for a border crossing there will <em>always</em> be
2 warnings emitted, with the [BorderCrossingWarning.distance_type] set to <code><a href="Enums/DistanceType.html#/s:7heresdk12DistanceTypeO5aheadyA2CmF">DistanceType.ahead</a></code> and <code><a href="Enums/DistanceType.html#/s:7heresdk12DistanceTypeO6passedyA2CmF">DistanceType.passed</a></code>
which is given when the location of the border crossing is reached.
A <code><a href="sdk-for-ios-navigate-structs-bordercrossingwarning">BorderCrossingWarning</a></code> will not be given until the previous warning of that type has been passed.
For example, a route with <code><a href="sdk-for-ios-navigate-structs-bordercrossingwarning">BorderCrossingWarning</a></code> 120 meters and <code><a href="sdk-for-ios-navigate-structs-bordercrossingwarning">BorderCrossingWarning</a></code> 160 meters ahead,
the first [BorderCrossingWarning.distance_to_border_crossing_in_meters] is 120 meters
and the next [BorderCrossingWarning.distance_to_border_crossing_in_meters] is then 40 meters,
since that is the distance between the first and second warnings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-bordercrossingwarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">BorderCrossingWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28BorderCrossingWarningOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/BorderCrossingWarningOptions"></a>
<a class="token" href="#/s:7heresdk28BorderCrossingWarningOptionsV">BorderCrossingWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Border crossing warning options.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-bordercrossingwarningoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BorderCrossingWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14CameraBehaviorP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/CameraBehavior"></a>
<a class="token" href="#/s:7heresdk14CameraBehaviorP">CameraBehavior</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol used to change implement different
camera behaviors.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-camerabehavior">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">CameraBehavior</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24CurrentSituationLaneViewV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CurrentSituationLaneView"></a>
<a class="token" href="#/s:7heresdk24CurrentSituationLaneViewV">CurrentSituationLaneView</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides current situation lane assistance view
information for the street at the current position of a single lane.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-currentsituationlaneview">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CurrentSituationLaneView</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk34CurrentSituationLaneAssistanceViewV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CurrentSituationLaneAssistanceView"></a>
<a class="token" href="#/s:7heresdk34CurrentSituationLaneAssistanceViewV">CurrentSituationLaneAssistanceView</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides current situation lane assistance view
information for the street at the current location.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-currentsituationlaneassistanceview">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CurrentSituationLaneAssistanceView</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk42CurrentSituationLaneAssistanceViewDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/CurrentSituationLaneAssistanceViewDelegate"></a>
<a class="token" href="#/s:7heresdk42CurrentSituationLaneAssistanceViewDelegateP">CurrentSituationLaneAssistanceViewDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be
implemented in order to receive notifications on <code><a href="sdk-for-ios-navigate-structs-currentsituationlaneassistanceview">CurrentSituationLaneAssistanceView</a></code>.</p>
<p>The current situation lane assistance view notifications describe the lane information at the current location.</p>
<p>A new notification is evaluated with each location update. A notification is only sent when there is a change
in lane data, such as a new upcoming lane.</p>
<p>This event is supported both with a route during turn-by-turn navigation and without a route in tracking mode.
During turn-by-turn navigation, the event additionally indicates which lanes help the driver stay on the route
to reach the destination.
However, the event does not indicate which exact lane the user is currently driving in.
The listener works for offline mode as well.</p>
<p><strong>Note:</strong></p>
<ul>
<li>Lane information is not available for all roads. It’s mostly available for roads with painted turn directions.</li>
<li>This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</li>
</ul>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-currentsituationlaneassistanceviewdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">CurrentSituationLaneAssistanceViewDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CustomPanningDataV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CustomPanningData"></a>
<a class="token" href="#/s:7heresdk17CustomPanningDataV">CustomPanningData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class contains all the information regarding the next angular panning element, including
a new estimated audio cue duration, and a new set of initial and sweep angular angle,
allowing the customization of the spatial audio trajectories for any type of notification,
such as speed or merge warners, maneuvers or even roundabouts notifications.
The orientation in space for <code><a href="Structs/CustomPanningData.html#/s:7heresdk17CustomPanningDataV23initialAzimuthInDegreesSdSgvp">CustomPanningData.initialAzimuthInDegrees</a></code> and <code><a href="Structs/CustomPanningData.html#/s:7heresdk17CustomPanningDataV21sweepAzimuthInDegreesSdSgvp">CustomPanningData.sweepAzimuthInDegrees</a></code> can
be represented by the following angular values:</p>
<table><thead>
<tr>
<th style="text-align: center">Front</th>
<th style="text-align: center">Right</th>
<th style="text-align: center">Rear</th>
<th style="text-align: center">Left</th>
</tr>
</thead><tbody>
<tr>
<td style="text-align: center">0°</td>
<td style="text-align: center">+90°</td>
<td style="text-align: center">+- 180</td>
<td style="text-align: center">-90°</td>
</tr>
</tbody></table>
<p>When any of the members of <code>CustomPanningData</code> are initialized as null, the default value
provided by HERE SDK will be used instead.
The audio cue is spatialized considering the action of both maneuvers, for example,
the audio cue ‘Now turn right and then turn left’ will be spatialized as following:
‘Now turn right’ will be heard as coming from the right.
‘and then turn left’ will be heard as coming from the left.
Note: The estimation for playing both audio cues could be not fully accurate and therefore
a mismatch between the audio source and the audio cue message could be perceived.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-custompanningdata">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CustomPanningData</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17DangerZoneWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DangerZoneWarning"></a>
<a class="token" href="#/s:7heresdk17DangerZoneWarningV">DangerZoneWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents danger zones. A danger zone refers to areas where there is an increased risk of
traffic incidents. These zones are designated to alert drivers to potential hazards and encourage
safer driving behaviors. Legally, certain devices can alert you to being in a danger zone,
typically indicating the presence of a speed camera. In line with applicable law and industry
standard, these alerts are usually provided along a road within a range of 4 km on a motorway,
2 km outside built-up areas, and 300 m in built-up areas​​. The HERE SDK warns when approaching
the danger zone, as well as when leaving such a zone. A danger zone may or may not have one or
more speed cameras in it. The exact location of such speed cameras is not provided. Note that
danger zones are only available in selected countries, such as France.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-dangerzonewarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DangerZoneWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25DangerZoneWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/DangerZoneWarningDelegate"></a>
<a class="token" href="#/s:7heresdk25DangerZoneWarningDelegateP">DangerZoneWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to receive notifications about the Danger zones.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-dangerzonewarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">DangerZoneWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26DestinationReachedDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/DestinationReachedDelegate"></a>
<a class="token" href="#/s:7heresdk26DestinationReachedDelegateP">DestinationReachedDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be
implemented in order to receive notifications from this class about the
arrival at the destination.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-destinationreacheddelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">DestinationReachedDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DimensionRestrictionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DimensionRestriction"></a>
<a class="token" href="#/s:7heresdk20DimensionRestrictionV">DimensionRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines a dimension restriction.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-dimensionrestriction">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DimensionRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24DimensionRestrictionTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/DimensionRestrictionType"></a>
<a class="token" href="#/s:7heresdk24DimensionRestrictionTypeO">DimensionRestrictionType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the type of a dimension restriction.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-dimensionrestrictiontype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">DimensionRestrictionType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31DirectionInformationUsageOptionO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/DirectionInformationUsageOption"></a>
<a class="token" href="#/s:7heresdk31DirectionInformationUsageOptionO">DirectionInformationUsageOption</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the option of direction information included in the notification.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-directioninformationusageoption">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">DirectionInformationUsageOption</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12DistanceTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/DistanceType"></a>
<a class="token" href="#/s:7heresdk12DistanceTypeO">DistanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><strong>Note:</strong> The distance types are being given for warnings at distances which can be configured
via options specific for each warner. These distances are defined based on the <code>sdk.navigation.TimingProfile</code>
calculated based on the speed limit present at the driver’s current location.
Indicates the distance type for a warning.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-distancetype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">DistanceType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13DividerMarkerO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/DividerMarker"></a>
<a class="token" href="#/s:7heresdk13DividerMarkerO">DividerMarker</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the divider between the lanes.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-dividermarker">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">DividerMarker</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21DynamicCameraBehaviorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/DynamicCameraBehavior"></a>
<a class="token" href="#/s:7heresdk21DynamicCameraBehaviorC">DynamicCameraBehavior</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Use this class to follow the current location of the user: The camera will look at
the target location that was fed into the navigator instance, gradually zooming in as the user
approaches each maneuver and zooming out after the user passes them. Since location updates
happen in discrete intervals, locations in-between will be interpolated to achieve a smooth
camera movement.  If no route is set, constant values of camera distance and tilt are used.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-dynamiccamerabehavior">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DynamicCameraBehavior</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-camerabehavior">CameraBehavior</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DynamicCameraBehavior</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DynamicCameraBehavior</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DynamicRoutingEngineC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/DynamicRoutingEngine"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC">DynamicRoutingEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class queries the HERE routing backend
to find routes with less traffic and therefore an earlier remaining estimated time of arrival.</p>
<p><code>DynamicRoutingEngine</code> polls the HERE routing backend periodically to find the best new route out
of a given initial route.
For initial route calculation it is recommended to use the <code><a href="sdk-for-ios-navigate-classes-routingengine">RoutingEngine</a></code>
as it already requests traffic-optimized routes.</p>
<p>When a better route is found, it is recommended to follow these steps to set the new route:</p>
<ol>
<li>Stop the <code>DynamicRoutingEngine</code>.</li>
<li>Update the currently active <code><a href="sdk-for-ios-navigate-classes-navigator">Navigator</a></code>instance with the newly found route.</li>
<li>Restart the <code>DynamicRoutingEngine</code>. This should be done outside of the <code>onBetterRouteFound()</code> callback.</li>
</ol>
<p>For both <code>DynamicRoutingEngine</code> and <code><a href="sdk-for-ios-navigate-classes-routingengine">RoutingEngine</a></code>,
the resulting routes are optimized based on speed flow changes such as traffic jams,
street closures or road accidents.
To get the best result, it is recommended to not specify the
<code><a href="Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">RouteOptions.departureTime</a></code> as then the current time is used by default.</p>
<p>The poll interval is defined by
<code><a href="Structs/DynamicRoutingEngineOptions.html#/s:7heresdk27DynamicRoutingEngineOptionsV12pollIntervalSdvp">DynamicRoutingEngineOptions.pollInterval</a></code> and
triggered by <code><a href="Classes/DynamicRoutingEngine.html#/s:7heresdk20DynamicRoutingEngineC21updateCurrentLocation010mapMatchedG012sectionIndexyAA03MapiG0V_s5Int32VtF">DynamicRoutingEngine.updateCurrentLocation(...)</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-dynamicroutingengine">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DynamicRoutingEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DynamicRoutingEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DynamicRoutingEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22DynamicRoutingDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/DynamicRoutingDelegate"></a>
<a class="token" href="#/s:7heresdk22DynamicRoutingDelegateP">DynamicRoutingDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to
receive notifications about the new route via the <code><a href="sdk-for-ios-navigate-classes-dynamicroutingengine">DynamicRoutingEngine</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-dynamicroutingdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">DynamicRoutingDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27DynamicRoutingEngineOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DynamicRoutingEngineOptions"></a>
<a class="token" href="#/s:7heresdk27DynamicRoutingEngineOptionsV">DynamicRoutingEngineOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options defining the behavior of the <code><a href="sdk-for-ios-navigate-classes-dynamicroutingengine">DynamicRoutingEngine</a></code>.
Both, <code>minTimeDifference</code> and <code>minTimeDifferencePercentage</code>, will be checked:
When the poll interval is reached, the smaller difference will win and
the <code><a href="sdk-for-ios-navigate-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a></code> is notified.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-dynamicroutingengineoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DynamicRoutingEngineOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24EnvironmentalZoneWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EnvironmentalZoneWarning"></a>
<a class="token" href="#/s:7heresdk24EnvironmentalZoneWarningV">EnvironmentalZoneWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents Environmental zones.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-environmentalzonewarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EnvironmentalZoneWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32EnvironmentalZoneWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/EnvironmentalZoneWarningDelegate"></a>
<a class="token" href="#/s:7heresdk32EnvironmentalZoneWarningDelegateP">EnvironmentalZoneWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to receive notifications about the environmental zones.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-environmentalzonewarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">EnvironmentalZoneWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9EventTextV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EventText"></a>
<a class="token" href="#/s:7heresdk9EventTextV">EventText</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains all the information regarding the next text announcement.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-eventtext">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EventText</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17EventTextDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/EventTextDelegate"></a>
<a class="token" href="#/s:7heresdk17EventTextDelegateP">EventTextDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to receive notifications
when text notifications are available from <code><a href="sdk-for-ios-navigate-classes-navigator">Navigator</a></code>. Multiple notifications
can be given for the same maneuver at different distances.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-eventtextdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">EventTextDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EventTextOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EventTextOptions"></a>
<a class="token" href="#/s:7heresdk16EventTextOptionsV">EventTextOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Text notifications options.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-eventtextoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EventTextOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19FixedCameraBehaviorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/FixedCameraBehavior"></a>
<a class="token" href="#/s:7heresdk19FixedCameraBehaviorC">FixedCameraBehavior</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Use this class to follow the current location of the user: The camera will permanently look at
the target location that was fed into the navigator instance. Since location updates happen in
discrete intervals, locations in-between will be interpolated to achieve a smooth camera
movement.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-fixedcamerabehavior">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">FixedCameraBehavior</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-camerabehavior">CameraBehavior</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">FixedCameraBehavior</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">FixedCameraBehavior</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26GeneralWarningRoadSignTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/GeneralWarningRoadSignType"></a>
<a class="token" href="#/s:7heresdk26GeneralWarningRoadSignTypeO">GeneralWarningRoadSignType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of a general warning that a road sign represents.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-generalwarningroadsigntype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">GeneralWarningRoadSignType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GPXDocumentC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/GPXDocument"></a>
<a class="token" href="#/s:7heresdk11GPXDocumentC">GPXDocument</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Use the GPXDocument to load the GPX file.
Only track data is used from the GPX file format
(see trkType at <a href="https://www.topografix.com/GPX/1/1/#type_trkType">https://www.topografix.com/GPX/1/1/#type_trkType</a>).
Any unknown elements in the file are ignored.
Any known element with an invalid value returns an error.
Elevation values are ignored.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-gpxdocument">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">GPXDocument</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXDocument</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXDocument</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10GPXOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GPXOptions"></a>
<a class="token" href="#/s:7heresdk10GPXOptionsV">GPXOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options used when reading the GPX file.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-gpxoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">GPXOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GPXTrackC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/GPXTrack"></a>
<a class="token" href="#/s:7heresdk8GPXTrackC">GPXTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Single track from the <code><a href="sdk-for-ios-navigate-classes-gpxdocument">GPXDocument</a></code>. Can be used as an input to the <code><a href="sdk-for-ios-navigate-classes-locationsimulator">LocationSimulator</a></code>.
Can be created and modified via <code><a href="sdk-for-ios-navigate-classes-gpxtrackwriter">GPXTrackWriter</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-gpxtrack">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">GPXTrack</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXTrack</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXTrack</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GPXTrackWriterC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/GPXTrackWriter"></a>
<a class="token" href="#/s:7heresdk14GPXTrackWriterC">GPXTrackWriter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Writes GPX track points to <code><a href="sdk-for-ios-navigate-classes-gpxtrack">GPXTrack</a></code>.
The instance of the class should be added as a listener to the
<code><a href="sdk-for-ios-navigate-classes-locationengine">LocationEngine</a></code> for GPX track recording.
Appends the new location to the back segment of the track whenever the listener is called.
The following data (if provided) can be recorded and inserted into the resulting <code><a href="sdk-for-ios-navigate-classes-gpxtrack">GPXTrack</a></code>: <code>latitude</code>, <code>longitude</code>, <code>altitude</code>, <code>time</code>, <code>bearingInDegrees</code>, <code>pitchInDegrees</code>, <code>speedInMetersPerSecond</code>, <code>horizontalAccuracyInMeters</code>, <code>verticalAccuracyInMeters</code>, <code>bearingAccuracyInDegrees</code>, <code>speedAccuracyInMetersPerSecond</code> and <code>locationTechnology</code>.</p>
<p>Use case examples:</p>
<p>A user wants to create and save a new <code><a href="sdk-for-ios-navigate-classes-gpxdocument">GPXDocument</a></code> with one <code><a href="sdk-for-ios-navigate-classes-gpxtrack">GPXTrack</a></code>:</p>
<ul>
<li>create <code>GPXTrackWriter</code> and add it as a location listener to <code><a href="sdk-for-ios-navigate-classes-locationengine">LocationEngine</a></code>.</li>
<li>set user parameters to <code><a href="Classes/GPXTrackWriter.html#/s:7heresdk14GPXTrackWriterC5trackAA0B0Cvp">GPXTrackWriter.track</a></code> (e.g. <code><a href="Classes/GPXTrack.html#/s:7heresdk8GPXTrackC4nameSSvp">GPXTrack.name</a></code> or <code><a href="Classes/GPXTrack.html#/s:7heresdk8GPXTrackC11descriptionSSvp">GPXTrack.description</a></code>).</li>
<li>when writing is completed, create a new <code><a href="sdk-for-ios-navigate-classes-gpxdocument">GPXDocument</a></code> with a list of one <code><a href="sdk-for-ios-navigate-classes-gpxtrack">GPXTrack</a></code> and save the document via <code><a href="Classes/GPXDocument.html#/s:7heresdk11GPXDocumentC4save11gpxFilePathSbSS_tF">GPXDocument.save(...)</a></code>.</li>
</ul>
<p>A user wants to modify and save <code><a href="sdk-for-ios-navigate-classes-gpxtrack">GPXTrack</a></code> in the existing <code><a href="sdk-for-ios-navigate-classes-gpxdocument">GPXDocument</a></code>:</p>
<ul>
<li>load <code><a href="sdk-for-ios-navigate-classes-gpxdocument">GPXDocument</a></code> from a file by the relevant constructor.</li>
<li>create <code>GPXTrackWriter</code> with the required track in the list <code><a href="Classes/GPXDocument.html#/s:7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp">GPXDocument.tracks</a></code>,
add the created instance as a location listener to <code><a href="sdk-for-ios-navigate-classes-locationengine">LocationEngine</a></code>.</li>
<li>when writing is completed, save the document via <code><a href="Classes/GPXDocument.html#/s:7heresdk11GPXDocumentC4save11gpxFilePathSbSS_tF">GPXDocument.save(...)</a></code>.</li>
</ul>
<p>The <code><a href="sdk-for-ios-navigate-classes-gpxdocument">GPXDocument</a></code> including all tracks is saved in the <a href="https://www.topografix.com/gpx.asp">GPX</a> file format. Hence, once saved, it can be easily shared with other applications that understand the GPX file format.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-gpxtrackwriter">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">GPXTrackWriter</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-locationdelegate">LocationDelegate</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXTrackWriter</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">GPXTrackWriter</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28InterpolatedLocationDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/InterpolatedLocationDelegate"></a>
<a class="token" href="#/s:7heresdk28InterpolatedLocationDelegateP">InterpolatedLocationDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented
in order to receive interpolated locations. The interpolated locations are only provided between
<code><a href="Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC14startRendering7mapViewyAA03MapG4Base_p_tF">VisualNavigator.startRendering(...)</a></code> and <code><a href="Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC13stopRenderingyyF">VisualNavigator.stopRendering(...)</a></code> calls and the application
is not running in the background.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-interpolatedlocationdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">InterpolatedLocationDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26JunctionViewLaneAssistanceV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/JunctionViewLaneAssistance"></a>
<a class="token" href="#/s:7heresdk26JunctionViewLaneAssistanceV">JunctionViewLaneAssistance</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides lane assistance information for the next complex junction
in order to keep following the route. It is recommended to indicate <code>JunctionViewLaneAssistance</code>
and <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code> separately or to indicate only <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code> information -
<code>JunctionViewLaneAssistance</code> will recommend all lanes that allow to pass the upcoming complex junction, regardless
if they will lead to the next maneuver or not.
If the location of a maneuver lies on an upcoming complex junction, the recommended lanes will be
the same as the ones from <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code>.</p>
<p>A junction is recognized as complex only if:</p>
<ul>
<li>it is at least a bifurcation;</li>
<li>it has at least two lanes whose directions do not follow the current route.
In opposition to <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code>, notifications are also forwarded when there is
no maneuver action occurring at the next complex junction.
Therefore, <code>JunctionViewLaneAssistance</code> can be disjointed from maneuvers. If lane assistance should be used to
associate it with upcoming maneuvers, consider to use <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code> instead.
Note that <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code> notifications are synchronized with maneuver events,
whereas <code>JunctionViewLaneAssistance</code> events are not strictly synchronized with maneuver events.</li>
</ul>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-junctionviewlaneassistance">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">JunctionViewLaneAssistance</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk34JunctionViewLaneAssistanceDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/JunctionViewLaneAssistanceDelegate"></a>
<a class="token" href="#/s:7heresdk34JunctionViewLaneAssistanceDelegateP">JunctionViewLaneAssistanceDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be
implemented in order to receive notifications on <code><a href="sdk-for-ios-navigate-structs-junctionviewlaneassistance">JunctionViewLaneAssistance</a></code>.
See <code><a href="sdk-for-ios-navigate-structs-junctionviewlaneassistance">JunctionViewLaneAssistance</a></code> documentation for further details.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-junctionviewlaneassistancedelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">JunctionViewLaneAssistanceDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4LaneV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Lane"></a>
<a class="token" href="#/s:7heresdk4LaneV">Lane</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides information for a lane.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-lane">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Lane</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LaneAccessV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LaneAccess"></a>
<a class="token" href="#/s:7heresdk10LaneAccessV">LaneAccess</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct which identifies the vehicle type(s) allowed to
access a lane.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-laneaccess">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LaneAccess</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13LaneDirectionO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LaneDirection"></a>
<a class="token" href="#/s:7heresdk13LaneDirectionO">LaneDirection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This enum defines the lane direction.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-lanedirection">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LaneDirection</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LaneDirectionCategoryV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LaneDirectionCategory"></a>
<a class="token" href="#/s:7heresdk21LaneDirectionCategoryV">LaneDirectionCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the directions of a lane. Most lanes lead only to one direction,
but there can be also lanes that split up into multiple directions.
A road can consist of multiple lanes towards the same direction.
Note: All members can be <code>true</code> or <code>false</code> at the same time. Lanes such as bicycle
lanes mostly never contain a direction category and thus, all members are <code>false</code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-lanedirectioncategory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LaneDirectionCategory</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12LaneMarkingsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LaneMarkings"></a>
<a class="token" href="#/s:7heresdk12LaneMarkingsV">LaneMarkings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides information for the lane markings.</p>
<p>Lane markings indicate the markings on the road.</p>
<p>Lane Divider Marker indicates the lane separator
on the right side of the specified lane in the lane driving direction for Right-side driving countries.
For left-sided driving countries the Lane Divider Marker is indicating the lane separator
on the left side of the specified lane in the lane driving direction.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-lanemarkings">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LaneMarkings</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23LaneRecommendationStateO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LaneRecommendationState"></a>
<a class="token" href="#/s:7heresdk23LaneRecommendationStateO">LaneRecommendationState</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates whether this lane leads to the next maneuvers or not.
The next maneuver is the next upcoming maneuver which is not yet reached, but
that was already announced as <em>new</em> maneuver in [sdk.navigation.RouteProgress.maneuver_progress].</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-lanerecommendationstate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LaneRecommendationState</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LaneTypeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LaneType"></a>
<a class="token" href="#/s:7heresdk8LaneTypeV">LaneType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides information on the available lane properties.
The lane type values can be combined as follows:</p>
<ul>
<li>High Occupancy Vehicle, Reversible</li>
<li>High Occupancy Vehicle and Express</li>
<li>Reversible and Express</li>
<li>High Occupancy Vehicle, Reversible and Express</li>
<li>High Occupancy Vehicle and Acceleration</li>
<li>Reversible, Acceleration Lane</li>
<li>High Occupancy Vehicle, Reversible, Acceleration Lane</li>
<li>Express and Acceleration</li>
<li>High Occupancy Vehicle and Deceleration</li>
<li>Reversible, Deceleration Lane</li>
<li>High Occupancy Vehicle, Reversible, Deceleration Lane</li>
<li>Express and Deceleration</li>
</ul>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-lanetype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LaneType</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LowSpeedZoneWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LowSpeedZoneWarning"></a>
<a class="token" href="#/s:7heresdk19LowSpeedZoneWarningV">LowSpeedZoneWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides low speed zone. The main field describing the low speed zone is <code>LowSpeedZoneWarning.speed_limit_in_meters_per_second</code>
specifying the speed limit of the low speed zone.
Use <code>LowSpeedZoneWarningListener</code> to get notifications about upcoming low speed zones.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-lowspeedzonewarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LowSpeedZoneWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27LowSpeedZoneWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/LowSpeedZoneWarningDelegate"></a>
<a class="token" href="#/s:7heresdk27LowSpeedZoneWarningDelegateP">LowSpeedZoneWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to receive low speed zone warnings.
<strong>Note:</strong> This is currently available <em>only</em> for Japan.
The low speed zone warner is a zone warner, which means that for a low speed zone there will <em>always</em>
be 3 warnings emitted, with the <code>LowSpeedZoneWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>, <code>DistanceType.REACHED</code>
and lastly <code>DistanceType.PASSED</code> when the end of the low speed zone is passed.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-lowspeedzonewarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">LowSpeedZoneWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverNotificationDetails"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationDetailsV">ManeuverNotificationDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class provides the information regarding the next maneuver to be triggered</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-maneuvernotificationdetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverNotificationDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverNotificationOptions"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV">ManeuverNotificationOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct containing all options to be used when generating maneuver notifications.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-maneuvernotificationoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverNotificationOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ManeuverNotificationTimingOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverNotificationTimingOptions"></a>
<a class="token" href="#/s:7heresdk33ManeuverNotificationTimingOptionsV">ManeuverNotificationTimingOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct defining timing and distance thresholds for maneuver notifications.</p>
<p>Setting custom values will impact the time when the notification for each supported <code><a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">ManeuverNotificationType</a></code> is sent - dependent on the <code><a href="sdk-for-ios-navigate-enums-timingprofile">TimingProfile</a></code>.</p>
<p><strong>Note:</strong> By default, notification thresholds depend on <code><a href="sdk-for-ios-navigate-enums-timingprofile">TimingProfile</a></code>. When custom values are set, then these rules will still apply.
The following rules apply for all transport modes:</p>
<ul>
<li>For <code><a href="Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code> timing profile, if the current speed limit is less than 62 m/h (100 km/h), then the notification thresholds for <code><a href="Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> timing profile will be used instead.</li>
<li>For <code><a href="Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> timing profile, if the current speed limit is less than 37 m/h (60 km/h), then the notification thresholds for <code><a href="Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code> timing profile will be used instead.</li>
<li>For <code><a href="Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code> timing profile the thresholds will be always used as specified.</li>
</ul>
<p>The timings follow a strict order:</p>
<ol>
<li><code><a href="Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code>: The first notification, it may be very far away (use 0 for farthest or earliest possible notification).</li>
<li><code><a href="Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">ManeuverNotificationType.reminder</a></code>: The second notification.</li>
<li><code><a href="Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">ManeuverNotificationType.distance</a></code>: A second reminder notification to take action.</li>
<li><code><a href="Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">ManeuverNotificationType.action</a></code>: Final notification, specifying the required action to be taken.</li>
</ol>
<p>Therefore, it is crucial that the set values do not violate the order: range &gt; reminder &gt; distance &gt; action.
For example, the following values are valid: range = 4000, reminder = 2500, distance = 1000, action = 400.
If <code><a href="Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a></code> is smaller than <code><a href="Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC16DistanceInMeterss5Int32Vvp">ManeuverNotificationTimingOptions.reminderNotificationDistanceInMeters</a></code> the new options will be
silently ignored and the previous values are kept.</p>
<p>You always have the choice to specify the thresholds for time or distance. For each <code><a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">ManeuverNotificationType</a></code> a
notification is only sent once, so the value that is reached first, wins. However, it is recommended to always update both, time
and distance values.
A configuration value of 0 is only allowed for <code><a href="Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a></code> and <code><a href="Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a></code>.
It means that the maneuver notifications of type <code><a href="Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code> should be generated as soon
as the maneuver location is known - no matter how far away it may be.
It’s impossible for the other types to have 0 as value due to the descending ordering rule mentioned above.</p>
<p>You can also specify the <code><a href="Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV06doubleC16DistanceInMeterss5Int32Vvp">ManeuverNotificationTimingOptions.doubleNotificationDistanceInMeters</a></code> threshold that determines the distance between two maneuvers that
should be merged into a single maneuver notification, for example, when they are very close to each other. Maneuvers below this
threshold will be merged like in this example: “After 300 meters turn right and then turn left.”.</p>
<p>Tip: To set the timings to the HERE SDK, you can first call <code>getManeuverNotificationTimingOptions()</code> to get the default values
for the desired combination of transport mode and timing profile. Then configure the timings, then set it back by calling the
<code>setManeuverNotificationTimingOptions()</code>.</p>
<p>Note: In the comment of each attribute, the term <code>Others</code> refers to non-pedestrian transport modes such as
<code><a href="Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>, <code><a href="Enums/TransportMode.html#/s:7heresdk13TransportModeO7bicycleyA2CmF">TransportMode.bicycle</a></code>, <code><a href="Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>.</p>
<p>Attention: The default values for <code><a href="Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> on <code><a href="Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code> are theoretical, as such
routes cannot be calculated with the HERE SDK as highways are forbidden for pedestrians.</p>
<p>Usage example:</p>
<pre class="highlight swift"><code><span class="c1">// Get current values or default values, if no values have been set before.</span>
<span class="kt">ManeuverNotificationTimingOptions</span> <span class="n">car_highway_timings</span> <span class="o">=</span> <span class="kt">Navigator</span><span class="o">.</span><span class="nf">getManeuverNotificationTimingOptions</span><span class="p">(</span><span class="kt">TransportMode</span><span class="o">.</span><span class="n">car</span><span class="p">,</span> <span class="kt">TimingProfile</span><span class="o">.</span><span class="kt">FAST_SPEED</span><span class="p">);</span>
<span class="c1">// Set a new value for a specific option and keep the previous or default values for the others.</span>
<span class="n">car_highway_timings</span><span class="o">.</span><span class="n">distanceNotificationDistanceInMeters</span> <span class="o">=</span> <span class="mi">1500</span><span class="p">;</span>
<span class="c1">// Apply the changes to Navigator (or VisualNavigator).</span>
<span class="kt">Navigator</span><span class="o">.</span><span class="nf">setManeuverNotificationTimingOptions</span><span class="p">(</span><span class="kt">TransportMode</span><span class="o">.</span><span class="n">car</span><span class="p">,</span> <span class="kt">TimingProfile</span><span class="o">.</span><span class="kt">FAST_SPEED</span><span class="p">,</span> <span class="n">car_fast_speed_timings</span><span class="p">);</span>
</code></pre>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverNotificationTimingOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ManeuverNotificationTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ManeuverNotificationType"></a>
<a class="token" href="#/s:7heresdk24ManeuverNotificationTypeO">ManeuverNotificationType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the type of the maneuver notification.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-maneuvernotificationtype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ManeuverNotificationType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16ManeuverProgressV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverProgress"></a>
<a class="token" href="#/s:7heresdk16ManeuverProgressV">ManeuverProgress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates a user’s progress to a <code><a href="sdk-for-ios-navigate-classes-maneuver">Maneuver</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-maneuverprogress">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverProgress</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ManeuverViewLaneAssistanceV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverViewLaneAssistance"></a>
<a class="token" href="#/s:7heresdk26ManeuverViewLaneAssistanceV">ManeuverViewLaneAssistance</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides lane assistance information for the next maneuver(s).
During turn-by-turn navigation lane assistance can help a driver to choose the recommended lanes
in order to complete the upcoming maneuvers.
The notifications are synchronized with the <code><a href="sdk-for-ios-navigate-protocols-eventtextdelegate">EventTextDelegate</a></code>.
<code><a href="sdk-for-ios-navigate-protocols-eventtextdelegate">EventTextDelegate</a></code> has 4 notification types for each maneuver:
Range, Reminder, Distance and Action.
Only the maneuver notification of type Distance will also notify a ManeuverViewLaneAssistance object
(e.g. “After 400 meters, turn right onto Invalidenstraße”).
The notification will not be sent when other types of maneuver notification are given.
The notification will not be sent when no lane data is available.
During tracking mode, no notifications are delivered.
This ManeuverViewLaneAssistance information is valid until the next maneuver is reached.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverViewLaneAssistance</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk34ManeuverViewLaneAssistanceDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/ManeuverViewLaneAssistanceDelegate"></a>
<a class="token" href="#/s:7heresdk34ManeuverViewLaneAssistanceDelegateP">ManeuverViewLaneAssistanceDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be
implemented in order to receive notifications on <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code>.
See <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code> documentation for further details.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-maneuverviewlaneassistancedelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">ManeuverViewLaneAssistanceDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMatchedLocationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MapMatchedLocation"></a>
<a class="token" href="#/s:7heresdk18MapMatchedLocationV">MapMatchedLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes a map-matched location in the world at a given time.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-mapmatchedlocation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapMatchedLocation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MilestoneV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Milestone"></a>
<a class="token" href="#/s:7heresdk9MilestoneV">Milestone</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents information about the waypoints along the route.</p>
<p>Note that this can include additional waypoints added during route
calculation that may not have been part of the original user-defined
waypoint list. For example, additional waypoints are added automatically
between sections that require a different transport mode like when taking a
ferry.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-milestone">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Milestone</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MilestoneStatusO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MilestoneStatus"></a>
<a class="token" href="#/s:7heresdk15MilestoneStatusO">MilestoneStatus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This enum represents the status of the <code><a href="sdk-for-ios-navigate-structs-milestone">Milestone</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-milestonestatus">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MilestoneStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23MilestoneStatusDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/MilestoneStatusDelegate"></a>
<a class="token" href="#/s:7heresdk23MilestoneStatusDelegateP">MilestoneStatusDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be
implemented in order to receive notifications from this class about the
arrival at each <code><a href="sdk-for-ios-navigate-structs-milestone">Milestone</a></code> or missing it.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-milestonestatusdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">MilestoneStatusDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MilestoneTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MilestoneType"></a>
<a class="token" href="#/s:7heresdk13MilestoneTypeO">MilestoneType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This enum represents the type of the <code><a href="sdk-for-ios-navigate-structs-milestone">Milestone</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-milestonetype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MilestoneType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19NaturalGuidanceTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/NaturalGuidanceType"></a>
<a class="token" href="#/s:7heresdk19NaturalGuidanceTypeO">NaturalGuidanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the type of the natural guidance element.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-naturalguidancetype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">NaturalGuidanceType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigableLocationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/NavigableLocation"></a>
<a class="token" href="#/s:7heresdk17NavigableLocationV">NavigableLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains all the relevant information on the current location.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-navigablelocation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">NavigableLocation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25NavigableLocationDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/NavigableLocationDelegate"></a>
<a class="token" href="#/s:7heresdk25NavigableLocationDelegateP">NavigableLocationDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to receive notifications
about the current location from <code><a href="sdk-for-ios-navigate-classes-navigator">Navigator</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-navigablelocationdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">NavigableLocationDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9NavigatorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Navigator"></a>
<a class="token" href="#/s:7heresdk9NavigatorC">Navigator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class provides the basic navigation functionality. It provides
notifications about current map-matched location updates (see <code><a href="sdk-for-ios-navigate-structs-navigablelocation">NavigableLocation</a></code>).
And, if a route has been set, about the route progress (see <code><a href="sdk-for-ios-navigate-structs-routeprogress">RouteProgress</a></code>),
route deviations (see <code><a href="sdk-for-ios-navigate-structs-routedeviation">RouteDeviation</a></code>) and maneuver notifications (see
<code><a href="sdk-for-ios-navigate-protocols-eventtextdelegate">EventTextDelegate</a></code>).</p>
<p>All transport modes are supported for turn-by-turn navigation, except for public transit.
Public transit routes may lead to unsafe and unexpected results.</p>
<p>Navigation support for bus routes can be sometimes a bit limited and bus lane assistance and
turn-by-turn bus instructions may not be as appropriate as expected.</p>
<p>The <code><a href="sdk-for-ios-navigate-enums-transportmode">TransportMode</a></code> is determined from the provided <code><a href="sdk-for-ios-navigate-classes-route">Route</a></code> instance,
but the actual <code><a href="sdk-for-ios-navigate-enums-sectiontransportmode">SectionTransportMode</a></code> can vary along a route, for example, when a
ferry must be taken. When no route is set, the <code><a href="sdk-for-ios-navigate-structs-navigablelocation">NavigableLocation</a></code> assumes a drive
scenario.</p>
<p>This class continuously reacts to new locations provided from a location source and acts as a
<code><a href="sdk-for-ios-navigate-protocols-locationdelegate">LocationDelegate</a></code>.
The accuracy of the positioning increases with the update frequency. At least one update per second
should be provided. More information can be found at <code>LocationAccuracy.NAVIGATION</code>.</p>
<p><strong>Note:</strong>
Even without provided locations, for example, while driving through a tunnel, this class
can interpolate missing location events and still send <code><a href="sdk-for-ios-navigate-structs-navigablelocation">NavigableLocation</a></code>,
<code><a href="sdk-for-ios-navigate-structs-routeprogress">RouteProgress</a></code> and maneuver notifications.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-navigator">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Navigator</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-navigatorprotocol">NavigatorProtocol</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Navigator</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Navigator</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17NavigatorProtocolP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/NavigatorProtocol"></a>
<a class="token" href="#/s:7heresdk17NavigatorProtocolP">NavigatorProtocol</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol provides the basic functionality needed to run a navigation session.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-navigatorprotocol">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">NavigatorProtocol</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-locationdelegate">LocationDelegate</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24NotificationFormatOptionO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/NotificationFormatOption"></a>
<a class="token" href="#/s:7heresdk24NotificationFormatOptionO">NotificationFormatOption</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the formatting option of phoneme included in the notification.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-notificationformatoption">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">NotificationFormatOption</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33OffRoadDestinationReachedDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/OffRoadDestinationReachedDelegate"></a>
<a class="token" href="#/s:7heresdk33OffRoadDestinationReachedDelegateP">OffRoadDestinationReachedDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be
implemented in order to receive notifications from this class about the
arrival at the off-road destination.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-offroaddestinationreacheddelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">OffRoadDestinationReachedDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15OffRoadProgressV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/OffRoadProgress"></a>
<a class="token" href="#/s:7heresdk15OffRoadProgressV">OffRoadProgress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the information needed to help the users to reach their off-road destination.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-offroadprogress">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">OffRoadProgress</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23OffRoadProgressDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/OffRoadProgressDelegate"></a>
<a class="token" href="#/s:7heresdk23OffRoadProgressDelegateP">OffRoadProgressDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to
receive notifications about the current off-road location from <code><a href="sdk-for-ios-navigate-classes-navigator">Navigator</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-offroadprogressdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">OffRoadProgressDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RealisticViewRasterImageV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RealisticViewRasterImage"></a>
<a class="token" href="#/s:7heresdk24RealisticViewRasterImageV">RealisticViewRasterImage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A realistic view. The fields describing the realistic view are
<code><a href="Structs/RealisticViewRasterImage.html#/s:7heresdk24RealisticViewRasterImageV09realisticc3PngE7Content10Foundation4DataVvp">RealisticViewRasterImage.realisticViewPngImageContent</a></code> contains a PNG image of the realistic view
and is represented as binary data.
<code>RealisticViewRasterImage.realisticViewType</code> indicates the type of the realistic view.
A valid realistic view contains a non-empty <code><a href="Structs/RealisticViewRasterImage.html#/s:7heresdk24RealisticViewRasterImageV09realisticc3PngE7Content10Foundation4DataVvp">RealisticViewRasterImage.realisticViewPngImageContent</a></code>.
Use <code>RealisticViewWarningListener</code> to get notifications with the realistic views of the upcoming realistic view.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-realisticviewrasterimage">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RealisticViewRasterImage</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RealisticViewVectorImageV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RealisticViewVectorImage"></a>
<a class="token" href="#/s:7heresdk24RealisticViewVectorImageV">RealisticViewVectorImage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A realistic view of a junction. The fields describing the realistic view are
<code><a href="Structs/RealisticViewVectorImage.html#/s:7heresdk24RealisticViewVectorImageV08junctionc3SvgE7ContentSSvp">RealisticViewVectorImage.junctionViewSvgImageContent</a></code> contains a SVG image of the junction view
represented as a string.
<code><a href="Structs/RealisticViewVectorImage.html#/s:7heresdk24RealisticViewVectorImageV011signpostSvgE7ContentSSvp">RealisticViewVectorImage.signpostSvgImageContent</a></code> contains an SVG image of the signpost corresponding
to the junction, also represented as a string.
A valid realistic view contains a non-empty <code><a href="Structs/RealisticViewVectorImage.html#/s:7heresdk24RealisticViewVectorImageV08junctionc3SvgE7ContentSSvp">RealisticViewVectorImage.junctionViewSvgImageContent</a></code> and a
non-empty <code><a href="Structs/RealisticViewVectorImage.html#/s:7heresdk24RealisticViewVectorImageV011signpostSvgE7ContentSSvp">RealisticViewVectorImage.signpostSvgImageContent</a></code>.
Use <code>RealisticViewWarningListener</code> to get notifications with the realistic views of the upcoming junctions.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-realisticviewvectorimage">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RealisticViewVectorImage</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RealisticViewWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RealisticViewWarning"></a>
<a class="token" href="#/s:7heresdk20RealisticViewWarningV">RealisticViewWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A realistic view notification. This notification is given for complex junctions and it includes a visual
representation of that junction, in order to help the user to better navigate it. When
<code><a href="Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp">RealisticViewWarning.distanceType</a></code> is <code><a href="Enums/DistanceType.html#/s:7heresdk12DistanceTypeO5aheadyA2CmF">DistanceType.ahead</a></code>, the <code><a href="Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewVectorImage</a></code> object
will be provided with the junction view and the signpost representations. For <code><a href="Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp">RealisticViewWarning.distanceType</a></code>
with value <code><a href="Enums/DistanceType.html#/s:7heresdk12DistanceTypeO6passedyA2CmF">DistanceType.passed</a></code>, the <code><a href="Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">RealisticViewWarning.realisticViewVectorImage</a></code> object will be null.
Use <code>RealisticViewWarningListener</code> to get notifications about the realistic views of the upcoming junctions.</p>
<p>Realistic view notifications require an online connection in order to function properly, or that the
junction or signpost map layer data is cached, installed or preloaded as part of a <code><a href="sdk-for-ios-navigate-structs-region">Region</a></code>.
This can be enabled via feature configurations.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-realisticviewwarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RealisticViewWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28RealisticViewWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/RealisticViewWarningDelegate"></a>
<a class="token" href="#/s:7heresdk28RealisticViewWarningDelegateP">RealisticViewWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol
should be implemented in order to receive realistic view warnings.</p>
<p>A <code><a href="sdk-for-ios-navigate-structs-realisticviewwarning">RealisticViewWarning</a></code> will not be given until the previous warning of that type has been passed.
For example, a route with <code><a href="sdk-for-ios-navigate-structs-realisticviewwarning">RealisticViewWarning</a></code> 120 meters and <code><a href="sdk-for-ios-navigate-structs-realisticviewwarning">RealisticViewWarning</a></code> 160 meters ahead,
the first <code><a href="Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV010distanceTobC8InMetersSdvp">RealisticViewWarning.distanceToRealisticViewInMeters</a></code> is 120 meters
and the next <code><a href="Structs/RealisticViewWarning.html#/s:7heresdk20RealisticViewWarningV010distanceTobC8InMetersSdvp">RealisticViewWarning.distanceToRealisticViewInMeters</a></code> is then 40 meters,
since that is the distance between the first and second warnings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-realisticviewwarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">RealisticViewWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27RealisticViewWarningOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RealisticViewWarningOptions"></a>
<a class="token" href="#/s:7heresdk27RealisticViewWarningOptionsV">RealisticViewWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Realistic view warning options. Set the options for filtering the realistic view notifications and
setting the realistic view notification distances based on the road type.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-realisticviewwarningoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RealisticViewWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RailwayCrossingWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RailwayCrossingWarning"></a>
<a class="token" href="#/s:7heresdk22RailwayCrossingWarningV">RailwayCrossingWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides railway crossing. The main field describing the railway crossing is <code><a href="Structs/RailwayCrossingWarning.html#/s:7heresdk22RailwayCrossingWarningV4typeAA05RoutebC4TypeOvp">RailwayCrossingWarning.type</a></code> specifying
whether the railway crossing is protected by a barrier or not.
Use <code>RailwayCrossingWarningListener</code> to get notifications about upcoming railway crossings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-railwaycrossingwarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RailwayCrossingWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30RailwayCrossingWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/RailwayCrossingWarningDelegate"></a>
<a class="token" href="#/s:7heresdk30RailwayCrossingWarningDelegateP">RailwayCrossingWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol
should be implemented in order to receive railway crossing warnings.
<strong>Note:</strong> The railway crossing warner can be either a zone warner or a point warner, depending
on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This
means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad
crossing is a zone warner then 3 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>,
<code>DistanceType.REACHED</code> and lastly <code>DistanceType.PASSED</code> when the end of the railway crossing is passed. In
case the railroad crossing is a point warner then 2 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code>
set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code> when the end of the railway crossing is passed.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-railwaycrossingwarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">RailwayCrossingWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18RoadClassificationO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RoadClassification"></a>
<a class="token" href="#/s:7heresdk18RoadClassificationO">RoadClassification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Classification of the surrounding road environment.
Note: This enum is in beta; its underlying layout is not stable
and may change without any deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-roadclassification">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RoadClassification</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RoadSignV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadSign"></a>
<a class="token" href="#/s:7heresdk8RoadSignV">RoadSign</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes a road sign.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-roadsign">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadSign</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RoadSignCategoryO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RoadSignCategory"></a>
<a class="token" href="#/s:7heresdk16RoadSignCategoryO">RoadSignCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Road sign category defining a general purpose of the sign.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-roadsigncategory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RoadSignCategory</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RoadSignTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RoadSignType"></a>
<a class="token" href="#/s:7heresdk12RoadSignTypeO">RoadSignType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A road sign type classifying road signs that can appear along a road.
Some signs are standardized and look the same in all countries, e.g. <code><a href="Enums/RoadSignType.html#/s:7heresdk12RoadSignTypeO04stopC0yA2CmF">RoadSignType.stopSign</a></code>.
In general, the visual appearance of the road signs can differ across countries.
Some road signs can be combined with other signs, like <code><a href="sdk-for-ios-navigate-enums-weathertype">WeatherType</a></code> signs. The road sign will be always shown topmost.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-roadsigntype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RoadSignType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadSignWarning"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV">RoadSignWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A road sign. The main field describing the sign is <code><a href="Structs/RoadSignWarning.html#/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp">RoadSignWarning.type</a></code>. Some road types are standardized, others can be country specific.
A valid road sign contains known <code><a href="Structs/RoadSignWarning.html#/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp">RoadSignWarning.type</a></code> or <code><a href="Structs/RoadSignWarning.html#/s:7heresdk15RoadSignWarningV8categoryAA0bC8CategoryOvp">RoadSignWarning.category</a></code>.
Use <code>RoadSignWarningListener</code> to get notifications with current road signs.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-roadsignwarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadSignWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23RoadSignWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/RoadSignWarningDelegate"></a>
<a class="token" href="#/s:7heresdk23RoadSignWarningDelegateP">RoadSignWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol
should be implemented in order to receive road sign warnings.
<strong>Note:</strong> The road sign warner is a point warner, which means that for a road sign there will <em>always</em> be
2 warnings emitted, with the [RoadSignWarning.distance_type] set to <code><a href="Enums/DistanceType.html#/s:7heresdk12DistanceTypeO5aheadyA2CmF">DistanceType.ahead</a></code> and <code><a href="Enums/DistanceType.html#/s:7heresdk12DistanceTypeO6passedyA2CmF">DistanceType.passed</a></code>
which is given when the location of the road sign is reached.
A <code><a href="sdk-for-ios-navigate-structs-roadsignwarning">RoadSignWarning</a></code> will not be given until the previous warning of that type has been passed.
For example, a route with <code><a href="sdk-for-ios-navigate-structs-roadsignwarning">RoadSignWarning</a></code> 120 meters and <code><a href="sdk-for-ios-navigate-structs-roadsignwarning">RoadSignWarning</a></code> 160 meters ahead,
the first [RoadSignWarning.distance_to_road_sign_in_meters] is 120 meters
and the next [RoadSignWarning.distance_to_road_sign_in_meters] is then 40 meters,
since that is the distance between the first and second warnings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-roadsignwarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">RoadSignWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RoadSignWarningOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadSignWarningOptions"></a>
<a class="token" href="#/s:7heresdk22RoadSignWarningOptionsV">RoadSignWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides road sign warning options. Set the options for filtering of road sign notifications.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-roadsignwarningoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadSignWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RoadSignVehicleTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RoadSignVehicleType"></a>
<a class="token" href="#/s:7heresdk19RoadSignVehicleTypeO">RoadSignVehicleType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle type for which a road sign is applicable.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-roadsignvehicletype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RoadSignVehicleType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17RoadTextsDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/RoadTextsDelegate"></a>
<a class="token" href="#/s:7heresdk17RoadTextsDelegateP">RoadTextsDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol
should be implemented in order to receive textual attributes of the current road.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-roadtextsdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">RoadTextsDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RouteDeviationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RouteDeviation"></a>
<a class="token" href="#/s:7heresdk14RouteDeviationV">RouteDeviation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains all the relevant information on a deviation from the route.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-routedeviation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteDeviation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RouteDeviationDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/RouteDeviationDelegate"></a>
<a class="token" href="#/s:7heresdk22RouteDeviationDelegateP">RouteDeviationDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to
receive notifications
about route deviations from <code><a href="sdk-for-ios-navigate-classes-navigator">Navigator</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-routedeviationdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">RouteDeviationDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RouteMatchedLocationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RouteMatchedLocation"></a>
<a class="token" href="#/s:7heresdk20RouteMatchedLocationV">RouteMatchedLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a location matched to a specific position on a navigation route.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-routematchedlocation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteMatchedLocation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RouteProgressV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RouteProgress"></a>
<a class="token" href="#/s:7heresdk13RouteProgressV">RouteProgress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains all the relevant information on the user’s progress along a route.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-routeprogress">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteProgress</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RouteProgressColorsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RouteProgressColors"></a>
<a class="token" href="#/s:7heresdk19RouteProgressColorsV">RouteProgressColors</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This struct contains colors for the route progress visualization.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-routeprogresscolors">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteProgressColors</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21RouteProgressDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/RouteProgressDelegate"></a>
<a class="token" href="#/s:7heresdk21RouteProgressDelegateP">RouteProgressDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to receive notifications
about the route progress from <code><a href="sdk-for-ios-navigate-classes-navigator">Navigator</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-routeprogressdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">RouteProgressDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SafetyCameraTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/SafetyCameraType"></a>
<a class="token" href="#/s:7heresdk16SafetyCameraTypeO">SafetyCameraType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the type of the safety camera.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-safetycameratype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SafetyCameraType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19SafetyCameraWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SafetyCameraWarning"></a>
<a class="token" href="#/s:7heresdk19SafetyCameraWarningV">SafetyCameraWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides safety camera warning information.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-safetycamerawarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SafetyCameraWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27SafetyCameraWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/SafetyCameraWarningDelegate"></a>
<a class="token" href="#/s:7heresdk27SafetyCameraWarningDelegateP">SafetyCameraWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol
should be implemented in order to receive notifications on safety cameras.
A <code><a href="sdk-for-ios-navigate-structs-safetycamerawarning">SafetyCameraWarning</a></code> will not be given until the previous warning of that type has been passed.
For example, a route with <code><a href="sdk-for-ios-navigate-structs-safetycamerawarning">SafetyCameraWarning</a></code> 120 meters and <code><a href="sdk-for-ios-navigate-structs-safetycamerawarning">SafetyCameraWarning</a></code> 160 meters ahead,
the first <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is 120 meters
and the next <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>
<p>When <code>SafetyCameraWarningListener</code> is enabled, a new set of text notifications (e.g. “Speed camera ahead”) will be trigger if any has been also enabled.
The updates for the same safety camera appear in order of the initial <code>DistanceType.AHEAD</code> event.
That is a first in first out approach is used when multiple safety cameras are reached or passed on the same location.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-safetycamerawarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">SafetyCameraWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26SafetyCameraWarningOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SafetyCameraWarningOptions"></a>
<a class="token" href="#/s:7heresdk26SafetyCameraWarningOptionsV">SafetyCameraWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Safety camera warning options. Set the options in order to enable them.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-safetycamerawarningoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SafetyCameraWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SchoolZoneWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SchoolZoneWarning"></a>
<a class="token" href="#/s:7heresdk17SchoolZoneWarningV">SchoolZoneWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A school zone warning which notifies about a school zone presence on road with a speed limit
different than the default speed limit applicable for cars.
Use <code>SchoolZoneWarningListener</code> to get notifications about school zones.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-schoolzonewarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SchoolZoneWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25SchoolZoneWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/SchoolZoneWarningDelegate"></a>
<a class="token" href="#/s:7heresdk25SchoolZoneWarningDelegateP">SchoolZoneWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to receive school zone warnings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-schoolzonewarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">SchoolZoneWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SchoolZoneWarningOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SchoolZoneWarningOptions"></a>
<a class="token" href="#/s:7heresdk24SchoolZoneWarningOptionsV">SchoolZoneWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>School zone warning options. Set the options for configuring of school zone notifications.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-schoolzonewarningoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SchoolZoneWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/c:@M@heresdk@objc(cs)SDKNavigationInitializer"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SDKNavigationInitializer"></a>
<a class="token" href="#/c:@M@heresdk@objc(cs)SDKNavigationInitializer">SDKNavigationInitializer</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Do not use this. This class is used to initialize internals of the SDK.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-sdknavigationinitializer">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SDKNavigationInitializer</span> <span class="p">:</span> <span class="kt">NSObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SectionProgressV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SectionProgress"></a>
<a class="token" href="#/s:7heresdk15SectionProgressV">SectionProgress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates a user’s progress along a <code><a href="sdk-for-ios-navigate-classes-section">Section</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-sectionprogress">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SectionProgress</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22SpatialAudioCuePanningC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SpatialAudioCuePanning"></a>
<a class="token" href="#/s:7heresdk22SpatialAudioCuePanningC">SpatialAudioCuePanning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Use the <code>SpatialAudioCuePanning</code> to notify each of the azimuths which compose a spatial audio
trajectory along the audio cue.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-spatialaudiocuepanning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SpatialAudioCuePanning</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SpatialAudioCuePanning</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SpatialAudioCuePanning</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26SpatialNotificationDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpatialNotificationDetails"></a>
<a class="token" href="#/s:7heresdk26SpatialNotificationDetailsV">SpatialNotificationDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class provides all the information for a spatial text notification, including the
maneuver data and extra data which is required to set the direction of spatialization
of the audio cue.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-spatialnotificationdetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpatialNotificationDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21SpatialTrajectoryDataV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpatialTrajectoryData"></a>
<a class="token" href="#/s:7heresdk21SpatialTrajectoryDataV">SpatialTrajectoryData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This struct provides all the information regarding an angular panning element, including the panning angle
and whether or not it is the last element on the spatial audio trajectory.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-spatialtrajectorydata">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpatialTrajectoryData</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SpeedBasedCameraBehavior"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC">SpeedBasedCameraBehavior</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Use this class to follow the current location of the user, zooming in and out and changing
camera tilt according to the current speed.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-speedbasedcamerabehavior">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SpeedBasedCameraBehavior</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-camerabehavior">CameraBehavior</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SpeedBasedCameraBehavior</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SpeedBasedCameraBehavior</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SpeedLimitV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpeedLimit"></a>
<a class="token" href="#/s:7heresdk10SpeedLimitV">SpeedLimit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the speed limit of the current road.
Speed limits that are described as conditional can be time-dependent. For time-dependent speed limits,
the HERE SDK internally reads the current device time and notifies only on speed limits
that are currently active.</p>
<p>It is recommended to use <code><a href="Structs/SpeedLimit.html#/s:7heresdk10SpeedLimitV09effectivebC17InMetersPerSecondSdSgyF">SpeedLimit.effectiveSpeedLimitInMetersPerSecond(...)</a></code> when
an application does not offer dedicated speed limit indicators for other cases, such as
weather-dependent speed limits.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-speedlimit">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpeedLimit</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18SpeedLimitDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/SpeedLimitDelegate"></a>
<a class="token" href="#/s:7heresdk18SpeedLimitDelegateP">SpeedLimitDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol
should be implemented in order to receive the speed limit of the current road.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-speedlimitdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">SpeedLimitDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpeedLimitOffsetV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpeedLimitOffset"></a>
<a class="token" href="#/s:7heresdk16SpeedLimitOffsetV">SpeedLimitOffset</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that represents two separate speed limit offsets for higher and lower speed limits.
A driver will be notified when the current driving speed is above the speed limit + offset.
Only one of the two offsets is used depending on the current speed limit.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-speedlimitoffset">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpeedLimitOffset</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20SpeedWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/SpeedWarningDelegate"></a>
<a class="token" href="#/s:7heresdk20SpeedWarningDelegateP">SpeedWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to receive notifications
when a speed limit on a road is exceeded or driving speed is restored back to normal.</p>
<p><strong>Note:</strong>
The warnings issued by this protocol
don’t take into account any temporary special speed limits. See <code>SpeedLimitListener</code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-speedwarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">SpeedWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19SpeedWarningOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpeedWarningOptions"></a>
<a class="token" href="#/s:7heresdk19SpeedWarningOptionsV">SpeedWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that contains all options to be used for the speed limit warnings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-speedwarningoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpeedWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18SpeedWarningStatusO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/SpeedWarningStatus"></a>
<a class="token" href="#/s:7heresdk18SpeedWarningStatusO">SpeedWarningStatus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This enum represents the status of the speed warning feature.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-speedwarningstatus">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SpeedWarningStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20TextNotificationTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TextNotificationType"></a>
<a class="token" href="#/s:7heresdk20TextNotificationTypeO">TextNotificationType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Different types of text notifications.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-textnotificationtype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TextNotificationType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TimingProfileO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TimingProfile"></a>
<a class="token" href="#/s:7heresdk13TimingProfileO">TimingProfile</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies the timing profile used for emitting notifications and warnings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-timingprofile">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TimingProfile</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9TollBoothV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollBooth"></a>
<a class="token" href="#/s:7heresdk9TollBoothV">TollBooth</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides information of a toll stop.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-tollbooth">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollBooth</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TollBoothLaneV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollBoothLane"></a>
<a class="token" href="#/s:7heresdk13TollBoothLaneV">TollBoothLane</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides information for a toll booth.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-tollboothlane">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollBoothLane</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20TollCollectionMethodO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TollCollectionMethod"></a>
<a class="token" href="#/s:7heresdk20TollCollectionMethodO">TollCollectionMethod</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Available payment methods.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-tollcollectionmethod">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TollCollectionMethod</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollStopV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollStop"></a>
<a class="token" href="#/s:7heresdk8TollStopV">TollStop</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides information for a toll stop with multiple toll booths.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-tollstop">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollStop</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TollStopWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TollStopWarningDelegate"></a>
<a class="token" href="#/s:7heresdk23TollStopWarningDelegateP">TollStopWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol
should be implemented in order to receive information on the upcoming toll booth structure.</p>
<p>The warner might also warn about gates/checkpoints for vignette, border checkpoints
and similar structures on the street.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.
A <code><a href="sdk-for-ios-navigate-structs-tollstop">TollStop</a></code> will not be given until the previous warning of that type has been passed.
For example, a route with <code><a href="sdk-for-ios-navigate-structs-tollstop">TollStop</a></code> 120 meters and <code><a href="sdk-for-ios-navigate-structs-tollstop">TollStop</a></code> 160 meters ahead,
the first <code>TollStop.distance_to_toll_stop_in_meters</code> is 120 meters
and the next <code>TollStop.distance_to_toll_stop_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-tollstopwarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TollStopWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrackingCameraBehavior"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC">TrackingCameraBehavior</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Use this class to follow a moving target. The camera smoothly tracks the target’s
position while adjusting heading, tilt, and zoom as needed. When tracking starts
or resumes, the camera first animates a re-centering transition to align with the target.</p>
<p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are
subject to change without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-trackingcamerabehavior">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrackingCameraBehavior</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-camerabehavior">CameraBehavior</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrackingCameraBehavior</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrackingCameraBehavior</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20TrafficMergeRoadTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TrafficMergeRoadType"></a>
<a class="token" href="#/s:7heresdk20TrafficMergeRoadTypeO">TrafficMergeRoadType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The type of road which is merging onto the current road.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-trafficmergeroadtype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TrafficMergeRoadType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficMergeSideO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TrafficMergeSide"></a>
<a class="token" href="#/s:7heresdk16TrafficMergeSideO">TrafficMergeSide</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The side from where the merging traffic is joining with the current highway.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-trafficmergeside">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TrafficMergeSide</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficMergeWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficMergeWarning"></a>
<a class="token" href="#/s:7heresdk19TrafficMergeWarningV">TrafficMergeWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides warning for merging traffic. The main field describing the merging traffic is <code>TrafficMergeWarning.road_type</code>
specifying the type of road containing traffic which is merging with the current road.
Use <code>TrafficMergeWarningListener</code> to get notifications about upcoming merging traffic.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-trafficmergewarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficMergeWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27TrafficMergeWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TrafficMergeWarningDelegate"></a>
<a class="token" href="#/s:7heresdk27TrafficMergeWarningDelegateP">TrafficMergeWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol
should be implemented in order to receive traffic merge warnings.
<strong>Note:</strong> The traffic merge warner is a point warner, which means that for a traffic merge there will <em>always</em> be
2 warnings emitted, with the <code>TrafficMergeWarning.distance_type</code> set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code>
which is given when the location of the traffic merge is reached.
A <code><a href="sdk-for-ios-navigate-structs-trafficmergewarning">TrafficMergeWarning</a></code> will not be given until the previous warning of that type has been passed.
For example, a route with <code><a href="sdk-for-ios-navigate-structs-trafficmergewarning">TrafficMergeWarning</a></code> 120 meters and <code><a href="sdk-for-ios-navigate-structs-trafficmergewarning">TrafficMergeWarning</a></code> 160 meters ahead,
the first <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is 120 meters
and the next <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-trafficmergewarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TrafficMergeWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26TrafficMergeWarningOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficMergeWarningOptions"></a>
<a class="token" href="#/s:7heresdk26TrafficMergeWarningOptionsV">TrafficMergeWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides traffic merge warning options. Set the options for filtering the traffic merge notifications.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-trafficmergewarningoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficMergeWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20TrafficOnRouteColorsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficOnRouteColors"></a>
<a class="token" href="#/s:7heresdk20TrafficOnRouteColorsV">TrafficOnRouteColors</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This type contains colors used for the traffic with jam factor greater or equal to 4.0 on route
ahead of the current location visualization.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-trafficonroutecolors">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficOnRouteColors</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TruckRestrictionWarningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TruckRestrictionWarning"></a>
<a class="token" href="#/s:7heresdk23TruckRestrictionWarningV">TruckRestrictionWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents truck restrictions. For example, there can be a bridge ahead not high enough to pass a big truck
or there can be a road ahead where the truck’s weight exceeds the permissible limit.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-truckrestrictionwarning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TruckRestrictionWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32TruckRestrictionsWarningDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TruckRestrictionsWarningDelegate"></a>
<a class="token" href="#/s:7heresdk32TruckRestrictionsWarningDelegateP">TruckRestrictionsWarningDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol
should be implemented in order to receive truck restriction warnings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-truckrestrictionswarningdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TruckRestrictionsWarningDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31TruckRestrictionsWarningOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TruckRestrictionsWarningOptions"></a>
<a class="token" href="#/s:7heresdk31TruckRestrictionsWarningOptionsV">TruckRestrictionsWarningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Truck restrictions warning options.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-truckrestrictionswarningoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TruckRestrictionsWarningOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VisualNavigatorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VisualNavigator"></a>
<a class="token" href="#/s:7heresdk15VisualNavigatorC">VisualNavigator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class provides all functionality of <code><a href="sdk-for-ios-navigate-protocols-navigatorprotocol">NavigatorProtocol</a></code>. In addition,
it provides advanced rendering capabilities for a smooth navigation experience.
This includes interpolation of location updates along a route during turn-by-turn navigation
and during tracking mode. By default, suitable map view settings are automatically applied.
For example, a predefined current location marker is rendered.
Similar to <code><a href="sdk-for-ios-navigate-classes-navigator">Navigator</a></code>, this class continuously reacts to new locations
provided from a location source and acts as a <code><a href="sdk-for-ios-navigate-protocols-locationdelegate">LocationDelegate</a></code>.
Note that the VisualNavigator takes control of the MapView’s (maximum) frame rate when rendering,
i.e., between <code><a href="Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC14startRendering7mapViewyAA03MapG4Base_p_tF">VisualNavigator.startRendering(...)</a></code> and <code><a href="Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC13stopRenderingyyF">VisualNavigator.stopRendering(...)</a></code> calls. It overwrites the MapView’s frame
rate when some camera behavior is set using the <code><a href="Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC17guidanceFrameRates5Int32Vvp">VisualNavigator.guidanceFrameRate</a></code>. When no camera behavior
is preset, the original MapView’s frame rate (the value prior to the <code><a href="Classes/VisualNavigator.html#/s:7heresdk15VisualNavigatorC14startRendering7mapViewyAA03MapG4Base_p_tF">VisualNavigator.startRendering(...)</a></code> call) will
be used. While the VisualNavigator is rendering, direct changes in the MapView’s frame rate can
lead to unexpected behavior and therefore should be avoided.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-visualnavigator">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VisualNavigator</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-navigatorprotocol">NavigatorProtocol</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VisualNavigator</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VisualNavigator</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VisualNavigatorColorsC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VisualNavigatorColors"></a>
<a class="token" href="#/s:7heresdk21VisualNavigatorColorsC">VisualNavigatorColors</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class contains colors used by <code><a href="sdk-for-ios-navigate-classes-visualnavigator">VisualNavigator</a></code> to render
the route and the maneuver arrow visualization.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-visualnavigatorcolors">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VisualNavigatorColors</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VisualNavigatorColors</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VisualNavigatorColors</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9WallClockP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/WallClock"></a>
<a class="token" href="#/s:7heresdk9WallClockP">WallClock</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Clock used to properly retrieve time-dependent data from the map.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-wallclock">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">WallClock</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28WarningNotificationDistancesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WarningNotificationDistances"></a>
<a class="token" href="#/s:7heresdk28WarningNotificationDistancesV">WarningNotificationDistances</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distances for emitting warnings according to the timing profile.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-warningnotificationdistances">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WarningNotificationDistances</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11WarningTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/WarningType"></a>
<a class="token" href="#/s:7heresdk11WarningTypeO">WarningType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies the warning type.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-warningtype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">WarningType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11WeatherTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/WeatherType"></a>
<a class="token" href="#/s:7heresdk11WeatherTypeO">WeatherType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Weather type attached to <code><a href="sdk-for-ios-navigate-structs-roadsignwarning">RoadSignWarning</a></code> or <code>VehicleRestriction.Condition</code> which limits the conditions for which the sign is applicable.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-weathertype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">WeatherType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17WeightRestrictionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WeightRestriction"></a>
<a class="token" href="#/s:7heresdk17WeightRestrictionV">WeightRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines a weight restriction.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-weightrestriction">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WeightRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21WeightRestrictionTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/WeightRestrictionType"></a>
<a class="token" href="#/s:7heresdk21WeightRestrictionTypeO">WeightRestrictionType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the type of a weight restriction.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-weightrestrictiontype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">WeightRestrictionType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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

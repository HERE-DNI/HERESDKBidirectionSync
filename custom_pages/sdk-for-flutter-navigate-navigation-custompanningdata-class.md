---
title: "CustomPanningData class"
slug: "sdk-for-flutter-navigate-navigation-custompanningdata-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomPanningData-class.html -->


<div>
<h1>CustomPanningData class</h1></div>

<p>This class contains all the information regarding the next angular panning element, including
a new estimated audio cue duration, and a new set of initial and sweep angular angle,
allowing the customization of the spatial audio trajectories for any type of notification,
such as speed or merge warners, maneuvers or even roundabouts notifications.</p>
<p>The orientation in space for <a href="sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees">CustomPanningData.initialAzimuthInDegrees</a> and <a href="sdk-for-flutter-navigate-navigation-custompanningdata-sweepazimuthindegrees">CustomPanningData.sweepAzimuthInDegrees</a> can
be represented by the following angular values:</p>
<table>
<thead>
<tr>
<th align="center">Front</th>
<th align="center">Right</th>
<th align="center">Rear</th>
<th align="center">Left</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">0°</td>
<td align="center">+90°</td>
<td align="center">+- 180</td>
<td align="center">-90°</td>
</tr>
</tbody>
</table>
<p>When any of the members of <a href="sdk-for-flutter-navigate-navigation-custompanningdata-class">CustomPanningData</a> are initialized as null, the default value
provided by HERE SDK will be used instead.
The audio cue is spatialized considering the action of both maneuvers, for example,
the audio cue 'Now turn right and then turn left' will be spatialized as following:
'Now turn right' will be heard as coming from the right.
'and then turn left' will be heard as coming from the left.
Note: The estimation for playing both audio cues could be not fully accurate and therefore
a mismatch between the audio source and the audio cue message could be perceived.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-custompanningdata-custompanningdata">CustomPanningData</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-custompanningdata-estimatedaudiocueduration">estimatedAudioCueDuration</a></li><li><a href="sdk-for-flutter-navigate-navigation-custompanningdata-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees">initialAzimuthInDegrees</a></li><li><a href="sdk-for-flutter-navigate-navigation-custompanningdata-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-navigate-navigation-custompanningdata-sweepazimuthindegrees">sweepAzimuthInDegrees</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-custompanningdata-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-navigation-custompanningdata-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-custompanningdata-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>

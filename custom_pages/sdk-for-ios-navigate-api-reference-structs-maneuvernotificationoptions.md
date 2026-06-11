---
title: "sdk-for-ios-navigate-api-reference-structs-maneuvernotificationoptions"
slug: "sdk-for-ios-navigate-api-reference-structs-maneuvernotificationoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverNotificationOptions"></a>
<a title="ManeuverNotificationOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>
<img alt="" id="carat" src="/carat.png"/>
        ManeuverNotificationOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ManeuverNotificationOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverNotificationOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct containing all options to be used when generating maneuver notifications.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV8languageAA12LanguageCodeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/language"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV8languageAA12LanguageCodeOvp">language</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The language in which the notifications will be generated. When the specified language
is not supported, the default language is used, which is English (American).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">language</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV10unitSystemAA04UnitF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/unitSystem"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV10unitSystemAA04UnitF0Ovp">unitSystem</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the measurement system used for distances. Defaults to metric.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">unitSystem</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-unitsystem">UnitSystem</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV08includedC5TypesSayAA0bC4TypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/includedNotificationTypes"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV08includedC5TypesSayAA0bC4TypeOGvp">includedNotificationTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of <code><a href="sdk-for-ios-navigate-api-reference-enums-maneuvernotificationtype">ManeuverNotificationType</a></code> for which notifications should be generated. Excluding all of
them will disable the maneuver notifications completely.
By default, all types are included.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">includedNotificationTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maneuvernotificationtype">ManeuverNotificationType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV016enableRoundaboutC0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/enableRoundaboutNotification"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV016enableRoundaboutC0Sbvp">enableRoundaboutNotification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that indicates whether notification for roundabout-related maneuvers should be generated.
Defaults to <code>true</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">enableRoundaboutNotification</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV024enableDestinationReachedC0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/enableDestinationReachedNotification"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV024enableDestinationReachedC0Sbvp">enableDestinationReachedNotification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that indicates whether notification for destination/stopover reached maneuvers should be generated.
Defaults to <code>true</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.27.0. Use the ManeuverNotificationOptions.arrivalNotificationOption instead")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">enableDestinationReachedNotification</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV07arrivalC6OptionAA07ArrivalcF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/arrivalNotificationOption"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV07arrivalC6OptionAA07ArrivalcF0Ovp">arrivalNotificationOption</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that indicates whether notification for destination and/or stopover reached maneuvers should be generated.
Defaults to <code>ArrivalNotificationOption.BOTH</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">arrivalNotificationOption</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-arrivalnotificationoption">ArrivalNotificationOption</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV012enableDoubleC0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/enableDoubleNotification"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV012enableDoubleC0Sbvp">enableDoubleNotification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that indicates whether combined maneuver notifications should be generated.
Such double notifications can be useful when maneuvers are very close.
<strong>Example:</strong> A combined message: ‘After 300 meters turn left and then turn right.’.
This way a user can better anticipate the next-next maneuver.
Note that setting to <code>true</code> will make the notification longer as two maneuvers will be merged into one.
When the next-next maneuver action takes place, the notification will be given as usual.
<strong>Example:</strong> ‘Now turn left and then then turn right.’ will be followed by ‘Now turn right.’.
Defaults to <code>true</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">enableDoubleNotification</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV13enablePhonemeSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/enablePhoneme"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV13enablePhonemeSbvp">enablePhoneme</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names,
road numbers, city names) should be used when generating notifications. Direction information comes usually
in orthographic form and phoneme (e.g. Wall Street and “wɔːl"striːt). However, when the notification is
synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability
and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of
direction information sound more natural.
<strong>Note:</strong> For now, this property is functional for road name and road number information only.
Moreover, the native <code>AVSpeechSynthesizer</code> for iOS does not support
phonemes as of now. Other 3rd party TTS engines may support it.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">enablePhoneme</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV24notificationFormatOptionAA0cfG0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/notificationFormatOption"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV24notificationFormatOptionAA0cfG0Ovp">notificationFormatOption</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A formatting option for the phoneme that is included in the notification. By default, no phoneme is used
and the <code><a href="../Enums/NotificationFormatOption.html#/s:7heresdk24NotificationFormatOptionO5plainyA2CmF">NotificationFormatOption.plain</a></code> orthographic form is included in the notification.</p>
<p><strong>Note:</strong>
To use the SSML format for phonemes, <code><a href="../Structs/ManeuverNotificationOptions.html#/s:7heresdk27ManeuverNotificationOptionsV13enablePhonemeSbvp">ManeuverNotificationOptions.enablePhoneme</a></code> needs to be set to <code>true</code>.
Moreover, the SSML format is not supported by the native <code>AVSpeechSynthesizer</code> for iOS, as of now.
Other 3rd party TTS engines may support it.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">notificationFormatOption</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-notificationformatoption">NotificationFormatOption</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV09textUsageD0AA04TextfD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textUsageOptions"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV09textUsageD0AA04TextfD0Vvp">textUsageOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An option whether street name, road number and sign post direction should be used when generating notification.
Defaults to each attribute as <code><a href="../Enums/LocalizedTextPreference.html#/s:7heresdk23LocalizedTextPreferenceO9useAlwaysyA2CmF">LocalizedTextPreference.useAlways</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">textUsageOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-textusageoptions">TextUsageOptions</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV17enableHighwayExitSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/enableHighwayExit"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV17enableHighwayExitSbvp">enableHighwayExit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that indicates whether highway exit information should be used when generating notification.
Defaults to <code>true</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">enableHighwayExit</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV24enableLaneRecommendationSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/enableLaneRecommendation"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV24enableLaneRecommendationSbvp">enableLaneRecommendation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that indicates whether lane recommendation should be used when generating notifications.
In case the flag is enabled, <em>only</em> the notification for the <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">ManeuverNotificationType.distance</a></code>
maneuver notification type will contain the lane recommendation. The lane recommandation will replace the
direction information in the notification.
<strong>Example:</strong> ‘After 250 meters use the right two lanes and turn right.’.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">enableLaneRecommendation</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV28includedNaturalGuidanceTypesSayAA0fG4TypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/includedNaturalGuidanceTypes"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV28includedNaturalGuidanceTypesSayAA0fG4TypeOGvp">includedNaturalGuidanceTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of <code><a href="sdk-for-ios-navigate-api-reference-enums-naturalguidancetype">NaturalGuidanceType</a></code> should be included in the notifications. Excluding
all of them will disable natural guidance information in the notifications completely.</p>
<p>By default, the list is empty and natural guidance is disabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">includedNaturalGuidanceTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-naturalguidancetype">NaturalGuidanceType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV034directionInformationUsageForActionC6OptionAA09DirectionfgJ0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/directionInformationUsageForActionNotificationOption"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV034directionInformationUsageForActionC6OptionAA09DirectionfgJ0Ovp">directionInformationUsageForActionNotificationOption</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An option whether direction information should be used when generating notification with
<code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">ManeuverNotificationType.action</a></code>. Defaults to <code><a href="../Enums/DirectionInformationUsageOption.html#/s:7heresdk31DirectionInformationUsageOptionO4noneyA2CmF">DirectionInformationUsageOption.none</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">directionInformationUsageForActionNotificationOption</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-directioninformationusageoption">DirectionInformationUsageOption</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsVACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsVACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class with default configurations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV8language10unitSystemAcA12LanguageCodeO_AA04UnitG0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(language:unitSystem:)"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV8language10unitSystemAcA12LanguageCodeO_AA04UnitG0Otcfc">init(language:<wbr/>unitSystem:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class with specified language and unit system.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.23.0. Use the default constructor instead.")</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">language</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span><span class="p">,</span> <span class="nv">unitSystem</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-unitsystem">UnitSystem</a></span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme09textUsageD00J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS4bAA04TextqD0VSbtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(language:unitSystem:includedNotificationTypes:enableRoundaboutNotification:enableDestinationReachedNotification:enableDoubleNotification:enablePhoneme:textUsageOptions:enableHighwayExit:)"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme09textUsageD00J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS4bAA04TextqD0VSbtcfc">init(language:<wbr/>unitSystem:<wbr/>includedNotificationTypes:<wbr/>enableRoundaboutNotification:<wbr/>enableDestinationReachedNotification:<wbr/>enableDoubleNotification:<wbr/>enablePhoneme:<wbr/>textUsageOptions:<wbr/>enableHighwayExit:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class with full specified configurations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.23.0. Use the default constructor instead.")</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">language</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span><span class="p">,</span> <span class="nv">unitSystem</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-unitsystem">UnitSystem</a></span><span class="p">,</span> <span class="nv">includedNotificationTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maneuvernotificationtype">ManeuverNotificationType</a></span><span class="p">],</span> <span class="nv">enableRoundaboutNotification</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">enableDestinationReachedNotification</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">enableDoubleNotification</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">enablePhoneme</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">textUsageOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-textusageoptions">TextUsageOptions</a></span><span class="p">,</span> <span class="nv">enableHighwayExit</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme0J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS5btcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(language:unitSystem:includedNotificationTypes:enableRoundaboutNotification:enableDestinationReachedNotification:enableDoubleNotification:enablePhoneme:enableHighwayExit:)"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme0J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS5btcfc">init(language:<wbr/>unitSystem:<wbr/>includedNotificationTypes:<wbr/>enableRoundaboutNotification:<wbr/>enableDestinationReachedNotification:<wbr/>enableDoubleNotification:<wbr/>enablePhoneme:<wbr/>enableHighwayExit:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class with full specified configurations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.23.0. Use the default constructor instead.")</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">language</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span><span class="p">,</span> <span class="nv">unitSystem</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-unitsystem">UnitSystem</a></span><span class="p">,</span> <span class="nv">includedNotificationTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maneuvernotificationtype">ManeuverNotificationType</a></span><span class="p">],</span> <span class="nv">enableRoundaboutNotification</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">enableDestinationReachedNotification</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">enableDoubleNotification</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">enablePhoneme</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">enableHighwayExit</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme24notificationFormatOption0J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS4bAA0cqR0OSbtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(language:unitSystem:includedNotificationTypes:enableRoundaboutNotification:enableDestinationReachedNotification:enableDoubleNotification:enablePhoneme:notificationFormatOption:enableHighwayExit:)"></a>
<a class="token" href="#/s:7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme24notificationFormatOption0J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS4bAA0cqR0OSbtcfc">init(language:<wbr/>unitSystem:<wbr/>includedNotificationTypes:<wbr/>enableRoundaboutNotification:<wbr/>enableDestinationReachedNotification:<wbr/>enableDoubleNotification:<wbr/>enablePhoneme:<wbr/>notificationFormatOption:<wbr/>enableHighwayExit:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class with full specified configurations.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>language: The language in which the notifications will be generated. When the specified language
is not supported, the default language is used, which is English (American).</li>
<li>unitSystem: Defines the measurement system used for distances. Defaults to metric.</li>
<li>includedNotificationTypes: List of <code><a href="sdk-for-ios-navigate-api-reference-enums-maneuvernotificationtype">ManeuverNotificationType</a></code> for which notifications should be generated. Excluding all of
them will disable the maneuver notifications completely.
By default, all types are included.</li>
<li>enableRoundaboutNotification: A flag that indicates whether notification for roundabout-related maneuvers should be generated.
Defaults to <code>true</code>.</li>
<li>enableDestinationReachedNotification: A flag that indicates whether notification for destination/stopover reached maneuvers should be generated.
Defaults to <code>true</code>.</li>
<li>enableDoubleNotification: A flag that indicates whether combined maneuver notifications should be generated.
Such double notifications can be useful when maneuvers are very close.
<strong>Example:</strong> A combined message: ‘After 300 meters turn left and then turn right.’.
This way a user can better anticipate the next-next maneuver.
Note that setting to <code>true</code> will make the notification longer as two maneuvers will be merged into one.
When the next-next maneuver action takes place, the notification will be given as usual.
<strong>Example:</strong> ‘Now turn left and then then turn right.’ will be followed by ‘Now turn right.’.
Defaults to <code>true</code>.</li>
<li>enablePhoneme: A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names,
road numbers, city names) should be used when generating notifications. Direction information comes usually
in orthographic form and phoneme (e.g. Wall Street and “wɔːl"striːt). However, when the notification is
synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability
and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of
direction information sound more natural.
<strong>Note:</strong> For now, this property is functional for road name and road number information only.
Moreover, the native <code>AVSpeechSynthesizer</code> for iOS does not support
phonemes as of now. Other 3rd party TTS engines may support it.
Defaults to <code>false</code>.</li>
<li>notificationFormatOption: A formatting option for the phoneme that is included in the notification. By default, no phoneme is used
and the <code><a href="../Enums/NotificationFormatOption.html#/s:7heresdk24NotificationFormatOptionO5plainyA2CmF">NotificationFormatOption.plain</a></code> orthographic form is included in the notification.</li>
</ul>
<p><strong>Note:</strong>
  To use the SSML format for phonemes, <code><a href="../Structs/ManeuverNotificationOptions.html#/s:7heresdk27ManeuverNotificationOptionsV13enablePhonemeSbvp">ManeuverNotificationOptions.enablePhoneme</a></code> needs to be set to <code>true</code>.
  Moreover, the SSML format is not supported by the native <code>AVSpeechSynthesizer</code> for iOS, as of now.
  Other 3rd party TTS engines may support it.</p>
<ul>
<li>enableHighwayExit: A flag that indicates whether highway exit information should be used when generating notification.
Defaults to <code>true</code>.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.23.0. Use the default constructor instead.")</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">language</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-languagecode">LanguageCode</a></span><span class="p">,</span> <span class="nv">unitSystem</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-unitsystem">UnitSystem</a></span><span class="p">,</span> <span class="nv">includedNotificationTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maneuvernotificationtype">ManeuverNotificationType</a></span><span class="p">],</span> <span class="nv">enableRoundaboutNotification</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">enableDestinationReachedNotification</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">enableDoubleNotification</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">enablePhoneme</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">notificationFormatOption</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-notificationformatoption">NotificationFormatOption</a></span><span class="p">,</span> <span class="nv">enableHighwayExit</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span></code></pre>
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
}</HTMLBlock>

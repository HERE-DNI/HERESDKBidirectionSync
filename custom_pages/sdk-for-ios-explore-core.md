---
title: "Core  Reference"
slug: "sdk-for-ios-explore-core"
---

<span id="//apple_ref/swift/Section/Core" class="dashAnchor"></span>

<div class="content-wrapper">

<a href="sdk-for-ios-explore-index">heresdk</a> <img src="img/carat.png" id="sdk-for-ios-explore-carat" /> Core Reference

</div>

<div class="content-wrapper">

<nav class="sidebar">

- <a href="sdk-for-ios-explore-core">Core</a>
  - <a href="sdk-for-ios-explore-structs-anchor2d">Anchor2D</a>
  - <a href="sdk-for-ios-explore-structs-anchor2dkeyframe">Anchor2DKeyframe</a>
  - <a href="sdk-for-ios-explore-classes-angle">Angle</a>
  - <a href="sdk-for-ios-explore-structs-anglerange">AngleRange</a>
  - <a href="sdk-for-ios-explore-classes-authentication">Authentication</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk31AuthenticationCompletionHandlera">AuthenticationCompletionHandler</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk23AuthenticationExceptiona">AuthenticationException</a>
  - <a href="sdk-for-ios-explore-classes-authenticationmode">AuthenticationMode</a>
  - <a href="sdk-for-ios-explore-structs-brandlogo">BrandLogo</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk30CacheCallbackCompletionHandlera">CacheCallbackCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-cardinaldirection">CardinalDirection</a>
  - <a href="sdk-for-ios-explore-structs-catalogconfiguration">CatalogConfiguration</a>
  - <a href="sdk-for-ios-explore-structs-catalogidentifier">CatalogIdentifier</a>
  - <a href="sdk-for-ios-explore-enums-catalogtype">CatalogType</a>
  - <a href="sdk-for-ios-explore-classes-catalogupdatetask">CatalogUpdateTask</a>
  - <a href="sdk-for-ios-explore-classes-catalogversionhint">CatalogVersionHint</a>
  - <a href="sdk-for-ios-explore-classes-collectionof">CollectionOf</a>
  - <a href="sdk-for-ios-explore-enums-countrycode">CountryCode</a>
  - <a href="sdk-for-ios-explore-enums-currenttype">CurrentType</a>
  - <a href="sdk-for-ios-explore-protocols-custommetadatavalue">CustomMetadataValue</a>
  - <a href="sdk-for-ios-explore-structs-desiredcatalog">DesiredCatalog</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk14DeviceIdHandlea">DeviceIdHandle</a>
  - <a href="sdk-for-ios-explore-enums-enginebaseurl">EngineBaseURL</a>
  - <a href="sdk-for-ios-explore-structs-engineoptions">EngineOptions</a>
  - <a href="sdk-for-ios-explore-structs-externalid">ExternalID</a>
  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>
  - <a href="sdk-for-ios-explore-structs-geocircle">GeoCircle</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a>
  - <a href="sdk-for-ios-explore-structs-geocorridor">GeoCorridor</a>
  - <a href="sdk-for-ios-explore-structs-geoorientation">GeoOrientation</a>
  - <a href="sdk-for-ios-explore-structs-geoorientationupdate">GeoOrientationUpdate</a>
  - <a href="sdk-for-ios-explore-structs-geopolygon">GeoPolygon</a>
  - <a href="sdk-for-ios-explore-structs-geopolyline">GeoPolyline</a>
  - <a href="sdk-for-ios-explore-enums-geopolylinedirection">GeoPolylineDirection</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk18InstantiationErrora">InstantiationError</a>
  - <a href="sdk-for-ios-explore-enums-instantiationerrorcode">InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-integerrange">IntegerRange</a>
  - <a href="sdk-for-ios-explore-enums-junctionstraversability">JunctionsTraversability</a>
  - <a href="sdk-for-ios-explore-enums-languagecode">LanguageCode</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration">LayerConfiguration</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature">– Feature</a>
  - <a href="sdk-for-ios-explore-structs-localizedroadnumber">LocalizedRoadNumber</a>
  - <a href="sdk-for-ios-explore-structs-localizedroadnumbers">LocalizedRoadNumbers</a>
  - <a href="sdk-for-ios-explore-structs-localizedtext">LocalizedText</a>
  - <a href="sdk-for-ios-explore-structs-localizedtexts">LocalizedTexts</a>
  - <a href="sdk-for-ios-explore-structs-location">Location</a>
  - <a href="sdk-for-ios-explore-protocols-locationdelegate">LocationDelegate</a>
  - <a href="sdk-for-ios-explore-enums-locationsource">LocationSource</a>
  - <a href="sdk-for-ios-explore-enums-locationtechnology">LocationTechnology</a>
  - <a href="sdk-for-ios-explore-structs-locationtime">LocationTime</a>
  - <a href="sdk-for-ios-explore-protocols-logappender">LogAppender</a>
  - <a href="sdk-for-ios-explore-classes-logcontrol">LogControl</a>
  - <a href="sdk-for-ios-explore-enums-loglevel">LogLevel</a>
  - <a href="sdk-for-ios-explore-classes-metadata">Metadata</a>
  - <a href="sdk-for-ios-explore-enums-metadatatype">MetadataType</a>
  - <a href="sdk-for-ios-explore-structs-nameid">NameID</a>
  - <a href="sdk-for-ios-explore-structs-networkendpoint">NetworkEndpoint</a>
  - <a href="sdk-for-ios-explore-structs-networksettings">NetworkSettings</a>
  - <a href="sdk-for-ios-explore-structs-parameterconfiguration">ParameterConfiguration</a>
  - <a href="sdk-for-ios-explore-enums-passthroughfeature">PassThroughFeature</a>
  - <a href="sdk-for-ios-explore-enums-powertype">PowerType</a>
  - <a href="sdk-for-ios-explore-structs-pedestrianprofile">PedestrianProfile</a>
  - <a href="sdk-for-ios-explore-structs-pickedplace">PickedPlace</a>
  - <a href="sdk-for-ios-explore-protocols-platformthreading">PlatformThreading</a>
  - <a href="sdk-for-ios-explore-structs-point2d">Point2D</a>
  - <a href="sdk-for-ios-explore-structs-point3d">Point3D</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk39PolylineSimplificationCompletionHandlera">PolylineSimplificationCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-polylinesimplificationerror">PolylineSimplificationError</a>
  - <a href="sdk-for-ios-explore-classes-polylinesimplifier">PolylineSimplifier</a>
  - <a href="sdk-for-ios-explore-classes-polylinesimplifier-options">– Options</a>
  - <a href="sdk-for-ios-explore-structs-proxysettings">ProxySettings</a>
  - <a href="sdk-for-ios-explore-structs-proxysettings-proxytype">– ProxyType</a>
  - <a href="sdk-for-ios-explore-structs-proxysettings-credentials">– Credentials</a>
  - <a href="sdk-for-ios-explore-structs-rectangle2d">Rectangle2D</a>
  - <a href="sdk-for-ios-explore-enums-routetype">RouteType</a>
  - <a href="sdk-for-ios-explore-protocols-runnable">Runnable</a>
  - <a href="sdk-for-ios-explore-classes-sdkbuildinformation">SDKBuildInformation</a>
  - <a href="sdk-for-ios-explore-classes-sdkcache">SDKCache</a>
  - <a href="sdk-for-ios-explore-classes-sdkinternalinitializer">SDKInternalInitializer</a>
  - <a href="sdk-for-ios-explore-classes-sdklogger">SDKLogger</a>
  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-classes-sdknativeengine-purgememorystrategy">– PurgeMemoryStrategy</a>
  - <a href="sdk-for-ios-explore-core#/c:@M@heresdk@objc(cs">SDKNativeEngineHolder</a>SDKNativeEngineHolder)
  - <a href="sdk-for-ios-explore-structs-sdkoptions">SDKOptions</a>
  - <a href="sdk-for-ios-explore-structs-sdkversion">SDKVersion</a>
  - <a href="sdk-for-ios-explore-structs-size2d">Size2D</a>
  - <a href="sdk-for-ios-explore-core#/s:SS">String</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>
  - <a href="sdk-for-ios-explore-enums-taskoutcome">TaskOutcome</a>
  - <a href="sdk-for-ios-explore-classes-threading">Threading</a>
  - <a href="sdk-for-ios-explore-classes-timerule">TimeRule</a>
  - <a href="sdk-for-ios-explore-structs-transportprofile">TransportProfile</a>
  - <a href="sdk-for-ios-explore-extensions-uicolor">UIColor</a>
  - <a href="sdk-for-ios-explore-enums-unitsystem">UnitSystem</a>
  - <a href="sdk-for-ios-explore-structs-usagestats">UsageStats</a>
  - <a href="sdk-for-ios-explore-structs-usagestats-feature">– Feature</a>
  - <a href="sdk-for-ios-explore-structs-usagestats-networkstats">– NetworkStats</a>
- <a href="sdk-for-ios-explore-electronichorizon">ElectronicHorizon</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizon">ElectronicHorizon</a>
  - <a href="sdk-for-ios-explore-classes-electronichorizondataloader">ElectronicHorizonDataLoader</a>
  - <a href="sdk-for-ios-explore-enums-electronichorizondataloadererrorcode">ElectronicHorizonDataLoaderErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizondataloaderresult">ElectronicHorizonDataLoaderResult</a>
  - <a href="sdk-for-ios-explore-enums-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a>
  - <a href="sdk-for-ios-explore-protocols-electronichorizondataloaderstatusdelegate">ElectronicHorizonDataLoaderStatusDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a>
  - <a href="sdk-for-ios-explore-classes-electronichorizonengine">ElectronicHorizonEngine</a>
  - <a href="sdk-for-ios-explore-enums-electronichorizonerrorcode">ElectronicHorizonErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonoptions">ElectronicHorizonOptions</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonpath">ElectronicHorizonPath</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonposition">ElectronicHorizonPosition</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonsegment">ElectronicHorizonSegment</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonsegmentchanges">ElectronicHorizonSegmentChanges</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonsegmentid">ElectronicHorizonSegmentId</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonupdate">ElectronicHorizonUpdate</a>
- <a href="sdk-for-ios-explore-ev">EV</a>
  - <a href="sdk-for-ios-explore-enums-evchargingconnectorformat">EVChargingConnectorFormat</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnectortype">EVChargingConnectorType</a>
  - <a href="sdk-for-ios-explore-enums-evsecapability">EVSECapability</a>
  - <a href="sdk-for-ios-explore-enums-evsepaymentsupport">EVSEPaymentSupport</a>
  - <a href="sdk-for-ios-explore-enums-evsestate">EVSEState</a>
- <a href="sdk-for-ios-explore-positioning">Positioning</a>
  - <a href="sdk-for-ios-explore-structs-authenticationdata">AuthenticationData</a>
  - <a href="sdk-for-ios-explore-enums-authenticationerror">AuthenticationError</a>
  - <a href="sdk-for-ios-explore-enums-confirmationstatus">ConfirmationStatus</a>
  - <a href="sdk-for-ios-explore-enums-locationaccuracy">LocationAccuracy</a>
  - <a href="sdk-for-ios-explore-protocols-locationenginebase">LocationEngineBase</a>
  - <a href="sdk-for-ios-explore-enums-locationenginestatus">LocationEngineStatus</a>
  - <a href="sdk-for-ios-explore-enums-locationfeature">LocationFeature</a>
  - <a href="sdk-for-ios-explore-classes-locationengine">LocationEngine</a>
  - <a href="sdk-for-ios-explore-classes-locationsimulator">LocationSimulator</a>
  - <a href="sdk-for-ios-explore-structs-locationsimulatoroptions">LocationSimulatorOptions</a>
  - <a href="sdk-for-ios-explore-protocols-locationstatusdelegate">LocationStatusDelegate</a>
- <a href="sdk-for-ios-explore-mapdata">MapData</a>
  - <a href="sdk-for-ios-explore-structs-administrativerules">AdministrativeRules</a>
  - <a href="sdk-for-ios-explore-classes-administrativerulesloader">AdministrativeRulesLoader</a>
  - <a href="sdk-for-ios-explore-structs-allowedtransportmodes">AllowedTransportModes</a>
  - <a href="sdk-for-ios-explore-structs-bloodalcoholcontentlimit">BloodAlcoholContentLimit</a>
  - <a href="sdk-for-ios-explore-structs-connectivity">Connectivity</a>
  - <a href="sdk-for-ios-explore-structs-directedocmsegmentid">DirectedOCMSegmentId</a>
  - <a href="sdk-for-ios-explore-structs-downloadingfileoptions">DownloadingFileOptions</a>
  - <a href="sdk-for-ios-explore-enums-drivingside">DrivingSide</a>
  - <a href="sdk-for-ios-explore-structs-filereference">FileReference</a>
  - <a href="sdk-for-ios-explore-enums-filereferencetype">FileReferenceType</a>
  - <a href="sdk-for-ios-explore-enums-headlightsrequirement">HeadlightsRequirement</a>
  - <a href="sdk-for-ios-explore-structs-laneattribute">LaneAttribute</a>
  - <a href="sdk-for-ios-explore-enums-localroadcharacteristic">LocalRoadCharacteristic</a>
  - <a href="sdk-for-ios-explore-mapdata#/s:7heresdk18MapDataLoaderErrora">MapDataLoaderError</a>
  - <a href="sdk-for-ios-explore-enums-mapdataloadererrorcode">MapDataLoaderErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-ocmsegmentid">OCMSegmentId</a>
  - <a href="sdk-for-ios-explore-enums-parkingsideregulation">ParkingSideRegulation</a>
  - <a href="sdk-for-ios-explore-structs-physicalattributes">PhysicalAttributes</a>
  - <a href="sdk-for-ios-explore-structs-pretripplanning">PreTripPlanning</a>
  - <a href="sdk-for-ios-explore-structs-railwaycrossing">RailwayCrossing</a>
  - <a href="sdk-for-ios-explore-enums-railwaycrossingtype">RailwayCrossingType</a>
  - <a href="sdk-for-ios-explore-enums-roaddivider">RoadDivider</a>
  - <a href="sdk-for-ios-explore-structs-roadusages">RoadUsages</a>
  - <a href="sdk-for-ios-explore-structs-segmentconnectivities">SegmentConnectivities</a>
  - <a href="sdk-for-ios-explore-classes-segmentdata">SegmentData</a>
  - <a href="sdk-for-ios-explore-classes-segmentdataloader">SegmentDataLoader</a>
  - <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a>
  - <a href="sdk-for-ios-explore-classes-segmentreferenceconverter">SegmentReferenceConverter</a>
  - <a href="sdk-for-ios-explore-classes-segmentspandata">SegmentSpanData</a>
  - <a href="sdk-for-ios-explore-structs-segmentspecialspeedsituation">SegmentSpecialSpeedSituation</a>
  - <a href="sdk-for-ios-explore-structs-segmentspeedlimit">SegmentSpeedLimit</a>
  - <a href="sdk-for-ios-explore-enums-specialspeedtype">SpecialSpeedType</a>
  - <a href="sdk-for-ios-explore-structs-tollcost">TollCost</a>
  - <a href="sdk-for-ios-explore-structs-tollpoint">TollPoint</a>
  - <a href="sdk-for-ios-explore-structs-tollstructure">TollStructure</a>
  - <a href="sdk-for-ios-explore-structs-tollstructuremaneuver">TollStructureManeuver</a>
  - <a href="sdk-for-ios-explore-enums-tollstructuretype">TollStructureType</a>
  - <a href="sdk-for-ios-explore-structs-tollsystem">TollSystem</a>
  - <a href="sdk-for-ios-explore-structs-trafficsignal">TrafficSignal</a>
  - <a href="sdk-for-ios-explore-enums-trafficsignallocation">TrafficSignalLocation</a>
  - <a href="sdk-for-ios-explore-enums-turnonredregulation">TurnOnRedRegulation</a>
- <a href="sdk-for-ios-explore-maploader">MapLoader</a>
  - <a href="sdk-for-ios-explore-structs-catalogupdateinfo">CatalogUpdateInfo</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk26CatalogsUpdateInfoCallbacka">CatalogsUpdateInfoCallback</a>
  - <a href="sdk-for-ios-explore-protocols-catalogupdateprogresslistener">CatalogUpdateProgressListener</a>
  - <a href="sdk-for-ios-explore-enums-catalogupdatestate">CatalogUpdateState</a>
  - <a href="sdk-for-ios-explore-enums-clientcertificaterequesttype">ClientCertificateRequestType</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk17CompletionHandlera">CompletionHandler</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk25ConfigureConnectionHandlea">ConfigureConnectionHandle</a>
  - <a href="sdk-for-ios-explore-protocols-dataattributesbase">DataAttributesBase</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk30DeleteRegionsCompletionHandlera">DeleteRegionsCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-downloadregionsstatuslistener">DownloadRegionsStatusListener</a>
  - <a href="sdk-for-ios-explore-classes-externalmapdatasourceclient">ExternalMapDataSourceClient</a>
  - <a href="sdk-for-ios-explore-enums-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk35ExternalMapDataSourceExceptionErrora">ExternalMapDataSourceExceptionError</a>
  - <a href="sdk-for-ios-explore-classes-externalmapdatasourceserver">ExternalMapDataSourceServer</a>
  - <a href="sdk-for-ios-explore-structs-installedcatalog">InstalledCatalog</a>
  - <a href="sdk-for-ios-explore-structs-installedregion">InstalledRegion</a>
  - <a href="sdk-for-ios-explore-enums-installedregionstatus">InstalledRegionStatus</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk8LineDataC">LineData</a>
  - <a href="sdk-for-ios-explore-classes-linedataaccessor">LineDataAccessor</a>
  - <a href="sdk-for-ios-explore-classes-linedatabuilder">LineDataBuilder</a>
  - <a href="sdk-for-ios-explore-classes-linedatasource">LineDataSource</a>
  - <a href="sdk-for-ios-explore-classes-linedatasourcebuilder">LineDataSourceBuilder</a>
  - <a href="sdk-for-ios-explore-enums-maploadererror">MapLoaderError</a>
  - <a href="sdk-for-ios-explore-classes-mapdownloader">MapDownloader</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk31MapDownloaderConstructionHandlea">MapDownloaderConstructionHandle</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk18MapLoaderExceptiona">MapLoaderException</a>
  - <a href="sdk-for-ios-explore-classes-mapdownloadertask">MapDownloaderTask</a>
  - <a href="sdk-for-ios-explore-protocols-mapupdateprogresslistener">MapUpdateProgressListener</a>
  - <a href="sdk-for-ios-explore-classes-mapupdater">MapUpdater</a>
  - <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy">– MapUpdateVersionCommitPolicy</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk29MapUpdaterConstructionHandlera">MapUpdaterConstructionHandler</a>
  - <a href="sdk-for-ios-explore-classes-mapupdatetask">MapUpdateTask</a>
  - <a href="sdk-for-ios-explore-classes-mapversionhandle">MapVersionHandle</a>
  - <a href="sdk-for-ios-explore-enums-navigabilitytype">NavigabilityType</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk25OfflineStorageSizeHandlera">OfflineStorageSizeHandler</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk23RepairCompletionHandlera">RepairCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-pemkeycertpair">PemKeyCertPair</a>
  - <a href="sdk-for-ios-explore-enums-persistentmaprepairerror">PersistentMapRepairError</a>
  - <a href="sdk-for-ios-explore-enums-persistentmapstatus">PersistentMapStatus</a>
  - <a href="sdk-for-ios-explore-structs-region">Region</a>
  - <a href="sdk-for-ios-explore-structs-regionid">RegionId</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk19ServerStartedHandlea">ServerStartedHandle</a>
  - <a href="sdk-for-ios-explore-structs-sslclientcredentialsoptions">SslClientCredentialsOptions</a>
  - <a href="sdk-for-ios-explore-structs-sslservercredentialsoptions">SslServerCredentialsOptions</a>
  - <a href="sdk-for-ios-explore-structs-updatestatistics">UpdateStatistics</a>
- <a href="sdk-for-ios-explore-mapmatcher">MapMatcher</a>
  - <a href="sdk-for-ios-explore-classes-mapmatcher">MapMatcher</a>
  - <a href="sdk-for-ios-explore-structs-matchedlocation">MatchedLocation</a>
- <a href="sdk-for-ios-explore-maps">Maps</a>
  - <a href="sdk-for-ios-explore-protocols-animationdelegate">AnimationDelegate</a>
  - <a href="sdk-for-ios-explore-enums-animationstate">AnimationState</a>
  - <a href="sdk-for-ios-explore-classes-assetsmanager">AssetsManager</a>
  - <a href="sdk-for-ios-explore-classes-dataattributes">DataAttributes</a>
  - <a href="sdk-for-ios-explore-classes-dataattributesaccessor">DataAttributesAccessor</a>
  - <a href="sdk-for-ios-explore-classes-dataattributesbuilder">DataAttributesBuilder</a>
  - <a href="sdk-for-ios-explore-classes-dataattributevalue">DataAttributeValue</a>
  - <a href="sdk-for-ios-explore-classes-dataattributevalue-valuetype">– ValueType</a>
  - <a href="sdk-for-ios-explore-structs-dashpattern">DashPattern</a>
  - <a href="sdk-for-ios-explore-protocols-doubletapdelegate">DoubleTapDelegate</a>
  - <a href="sdk-for-ios-explore-enums-drawordertype">DrawOrderType</a>
  - <a href="sdk-for-ios-explore-classes-easing">Easing</a>
  - <a href="sdk-for-ios-explore-classes-easing-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-enums-easingfunction">EasingFunction</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinateskeyframe">GeoCoordinatesKeyframe</a>
  - <a href="sdk-for-ios-explore-structs-geoorientationkeyframe">GeoOrientationKeyframe</a>
  - <a href="sdk-for-ios-explore-enums-gesturestate">GestureState</a>
  - <a href="sdk-for-ios-explore-enums-gesturetype">GestureType</a>
  - <a href="sdk-for-ios-explore-classes-gestures">Gestures</a>
  - <a href="sdk-for-ios-explore-classes-heremap">HereMap</a>
  - <a href="sdk-for-ios-explore-classes-iconprovider">IconProvider</a>
  - <a href="sdk-for-ios-explore-enums-iconproviderassettype">IconProviderAssetType</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk20IconProviderCallbacka">IconProviderCallback</a>
  - <a href="sdk-for-ios-explore-enums-iconprovidererror">IconProviderError</a>
  - <a href="sdk-for-ios-explore-enums-imageformat">ImageFormat</a>
  - <a href="sdk-for-ios-explore-classes-jsonstylefactory">JsonStyleFactory</a>
  - <a href="sdk-for-ios-explore-classes-jsonstylefactory-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-jsonstylefactory-instantiationerrordetails">– InstantiationErrorDetails</a>
  - <a href="sdk-for-ios-explore-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>
  - <a href="sdk-for-ios-explore-enums-linecap">LineCap</a>
  - <a href="sdk-for-ios-explore-classes-linetiledatasource">LineTileDataSource</a>
  - <a href="sdk-for-ios-explore-protocols-linetilesource">LineTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-linetilesourceloadresulthandler">LineTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-classes-locationindicator">LocationIndicator</a>
  - <a href="sdk-for-ios-explore-classes-locationindicator-indicatorstyle">– IndicatorStyle</a>
  - <a href="sdk-for-ios-explore-classes-locationindicator-markertype">– MarkerType</a>
  - <a href="sdk-for-ios-explore-protocols-longpressdelegate">LongPressDelegate</a>
  - <a href="sdk-for-ios-explore-classes-maparrow">MapArrow</a>
  - <a href="sdk-for-ios-explore-classes-mapcamera">MapCamera</a>
  - <a href="sdk-for-ios-explore-classes-mapcamera-state">– State</a>
  - <a href="sdk-for-ios-explore-classes-mapcamera-farplaneconfiguration">– FarPlaneConfiguration</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraanimation">MapCameraAnimation</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraanimationfactory">MapCameraAnimationFactory</a>
  - <a href="sdk-for-ios-explore-protocols-mapcameradelegate">MapCameraDelegate</a>
  - <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack">MapCameraKeyframeTrack</a>
  - <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcameralimits">MapCameraLimits</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraupdate">MapCameraUpdate</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraupdate-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraupdatefactory">MapCameraUpdateFactory</a>
  - <a href="sdk-for-ios-explore-enums-mapcontentcategory">MapContentCategory</a>
  - <a href="sdk-for-ios-explore-classes-mapcontentsettings">MapContentSettings</a>
  - <a href="sdk-for-ios-explore-classes-mapcontentsettings-trafficrefreshperioderrorcode">– TrafficRefreshPeriodErrorCode</a>
  - <a href="sdk-for-ios-explore-enums-mapcontenttype">MapContentType</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext">MapContext</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementstrategy">– MemoryManagementStrategy</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresultcode">– MemoryManagementResultCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-resourcetype">– ResourceType</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-freeresourceseverity">– FreeResourceSeverity</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresult">– MemoryManagementResult</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementoptions">– MemoryManagementOptions</a>
  - <a href="sdk-for-ios-explore-enums-maperror">MapError</a>
  - <a href="sdk-for-ios-explore-structs-mapfeatures">MapFeatures</a>
  - <a href="sdk-for-ios-explore-structs-mapfeaturemodes">MapFeatureModes</a>
  - <a href="sdk-for-ios-explore-protocols-mapidledelegate">MapIdleDelegate</a>
  - <a href="sdk-for-ios-explore-classes-mapimage">MapImage</a>
  - <a href="sdk-for-ios-explore-classes-mapimageoverlay">MapImageOverlay</a>
  - <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack">MapItemKeyFrameTrack</a>
  - <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk21MapItemRepresentationC">MapItemRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-maplayer">MapLayer</a>
  - <a href="sdk-for-ios-explore-classes-maplayerbuilder">MapLayerBuilder</a>
  - <a href="sdk-for-ios-explore-classes-maplayerbuilder-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-maplayerbuilder-instantiationerrordetails">– InstantiationErrorDetails</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a>
  - <a href="sdk-for-ios-explore-classes-maplayerprioritybuilder">MapLayerPriorityBuilder</a>
  - <a href="sdk-for-ios-explore-classes-maplayermapmeasuredependentstoragelevels">MapLayerMapMeasureDependentStorageLevels</a>
  - <a href="sdk-for-ios-explore-structs-maplayervisibilityrange">MapLayerVisibilityRange</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster">MapMarkerCluster</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster-grouping">– Grouping</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster-imagestyle">– ImageStyle</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster-counterstyle">– CounterStyle</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasurerange">MapMeasureRange</a>
  - <a href="sdk-for-ios-explore-classes-mapobjectdescriptor">MapObjectDescriptor</a>
  - <a href="sdk-for-ios-explore-enums-mapprojection">MapProjection</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights">MapSceneLights</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights-category">– Category</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights-attributesettingerror">– AttributeSettingError</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights-direction">– Direction</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a>
  - <a href="sdk-for-ios-explore-classes-mapsceneloadoptionsbuilder">MapSceneLoadOptionsBuilder</a>
  - <a href="sdk-for-ios-explore-classes-mapsceneloadoptionsbuilder-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapsceneloadoptionsbuilder-instantiationerrordetails">– InstantiationErrorDetails</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker">MapMarker</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker-textstyle">– TextStyle</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker3d">MapMarker3D</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker3dmodel">MapMarker3DModel</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker3dmodel-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkeranimation">MapMarkerAnimation</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkeranimation-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasure">MapMeasure</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasure-kind">– Kind</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mappolygon">MapPolygon</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-representation">– Representation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation">– DashImageRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-solidrepresentation">– SolidRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation">– DashRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-solidmulticolorrepresentation">– SolidMultiColorRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolylineanimation">MapPolylineAnimation</a>
  - <a href="sdk-for-ios-explore-classes-mappolylineanimation-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mappickresult">MapPickResult</a>
  - <a href="sdk-for-ios-explore-classes-mapscene">MapScene</a>
  - <a href="sdk-for-ios-explore-classes-mapscene-mappickfilter">– MapPickFilter</a>
  - <a href="sdk-for-ios-explore-enums-mapscheme">MapScheme</a>
  - <a href="sdk-for-ios-explore-protocols-mapviewbase">MapViewBase</a>
  - <a href="sdk-for-ios-explore-classes-mapview">MapView</a>
  - <a href="sdk-for-ios-explore-classes-mapview-viewpin">– ViewPin</a>
  - <a href="sdk-for-ios-explore-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a>
  - <a href="sdk-for-ios-explore-structs-mapviewoptions">MapViewOptions</a>
  - <a href="sdk-for-ios-explore-structs-materialreflectivity">MaterialReflectivity</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk4MeshC">Mesh</a>
  - <a href="sdk-for-ios-explore-classes-meshbuilder">MeshBuilder</a>
  - <a href="sdk-for-ios-explore-protocols-pandelegate">PanDelegate</a>
  - <a href="sdk-for-ios-explore-classes-pickmapcontentresult">PickMapContentResult</a>
  - <a href="sdk-for-ios-explore-classes-pickmapcontentresult-trafficincidentresult">– TrafficIncidentResult</a>
  - <a href="sdk-for-ios-explore-classes-pickmapcontentresult-vehiclerestrictionresult">– VehicleRestrictionResult</a>
  - <a href="sdk-for-ios-explore-classes-pickmapitemsresult">PickMapItemsResult</a>
  - <a href="sdk-for-ios-explore-protocols-pinchrotatedelegate">PinchRotateDelegate</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk9PointDataC">PointData</a>
  - <a href="sdk-for-ios-explore-classes-pointdataaccessor">PointDataAccessor</a>
  - <a href="sdk-for-ios-explore-classes-pointdatabuilder">PointDataBuilder</a>
  - <a href="sdk-for-ios-explore-classes-pointdatasource">PointDataSource</a>
  - <a href="sdk-for-ios-explore-classes-pointdatasourcebuilder">PointDataSourceBuilder</a>
  - <a href="sdk-for-ios-explore-classes-pointtiledatasource">PointTileDataSource</a>
  - <a href="sdk-for-ios-explore-protocols-pointtilesource">PointTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-pointtilesourceloadresulthandler">PointTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-structs-point2dkeyframe">Point2DKeyframe</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk11PolygonDataC">PolygonData</a>
  - <a href="sdk-for-ios-explore-classes-polygondataaccessor">PolygonDataAccessor</a>
  - <a href="sdk-for-ios-explore-classes-polygondatabuilder">PolygonDataBuilder</a>
  - <a href="sdk-for-ios-explore-classes-polygondatasource">PolygonDataSource</a>
  - <a href="sdk-for-ios-explore-classes-polygondatasourcebuilder">PolygonDataSourceBuilder</a>
  - <a href="sdk-for-ios-explore-classes-polygontiledatasource">PolygonTileDataSource</a>
  - <a href="sdk-for-ios-explore-protocols-polygontilesource">PolygonTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-polygontilesourceloadresulthandler">PolygonTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-classes-quadmeshbuilder">QuadMeshBuilder</a>
  - <a href="sdk-for-ios-explore-classes-rasterdatasource">RasterDataSource</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration">RasterDataSourceConfiguration</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-provider">– Provider</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-cache">– Cache</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfigurationupdate">RasterDataSourceConfigurationUpdate</a>
  - <a href="sdk-for-ios-explore-protocols-rasterdatasourcedelegate">RasterDataSourceDelegate</a>
  - <a href="sdk-for-ios-explore-enums-rasterdatasourceerror">RasterDataSourceError</a>
  - <a href="sdk-for-ios-explore-protocols-rastertilesource">RasterTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-rastertilesourceloadresulthandler">RasterTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-structs-roadshieldiconproperties">RoadShieldIconProperties</a>
  - <a href="sdk-for-ios-explore-structs-rendersize">RenderSize</a>
  - <a href="sdk-for-ios-explore-structs-rendersize-unit">– Unit</a>
  - <a href="sdk-for-ios-explore-structs-scalarkeyframe">ScalarKeyframe</a>
  - <a href="sdk-for-ios-explore-classes-sdkmapviewinitializer">SDKMapViewInitializer</a>
  - <a href="sdk-for-ios-explore-enums-shadowquality">ShadowQuality</a>
  - <a href="sdk-for-ios-explore-classes-style">Style</a>
  - <a href="sdk-for-ios-explore-protocols-tapdelegate">TapDelegate</a>
  - <a href="sdk-for-ios-explore-classes-tilegeoboundscalculator">TileGeoBoundsCalculator</a>
  - <a href="sdk-for-ios-explore-protocols-tilesource">TileSource</a>
  - <a href="sdk-for-ios-explore-structs-tilesourcedataversion">TileSourceDataVersion</a>
  - <a href="sdk-for-ios-explore-protocols-tilesourcedelegate">TileSourceDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-tilesourceloadtilerequesthandle">TileSourceLoadTileRequestHandle</a>
  - <a href="sdk-for-ios-explore-structs-tilesourcetilemetadata">TileSourceTileMetadata</a>
  - <a href="sdk-for-ios-explore-structs-tilekey">TileKey</a>
  - <a href="sdk-for-ios-explore-classes-tileurlproviderfactory">TileUrlProviderFactory</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk21TileUrlRequestHandlera">TileUrlRequestHandler</a>
  - <a href="sdk-for-ios-explore-enums-tilingscheme">TilingScheme</a>
  - <a href="sdk-for-ios-explore-classes-translucentmaplayergroup">TranslucentMapLayerGroup</a>
  - <a href="sdk-for-ios-explore-classes-translucentmaplayergroup-errorcode">– ErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-translucentmaplayergroup-errordetails">– ErrorDetails</a>
  - <a href="sdk-for-ios-explore-classes-trianglemeshbuilder">TriangleMeshBuilder</a>
  - <a href="sdk-for-ios-explore-protocols-twofingerpandelegate">TwoFingerPanDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-twofingertapdelegate">TwoFingerTapDelegate</a>
  - <a href="sdk-for-ios-explore-enums-visibilitystate">VisibilityState</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestrictioniconproperties">VehicleRestrictionIconProperties</a>
  - <a href="sdk-for-ios-explore-enums-watermarkstyle">WatermarkStyle</a>
- <a href="sdk-for-ios-explore-routing">Routing</a>
  - <a href="sdk-for-ios-explore-enums-accessattributes">AccessAttributes</a>
  - <a href="sdk-for-ios-explore-structs-agency">Agency</a>
  - <a href="sdk-for-ios-explore-structs-allowoptions">AllowOptions</a>
  - <a href="sdk-for-ios-explore-structs-attribution">Attribution</a>
  - <a href="sdk-for-ios-explore-enums-attributiontype">AttributionType</a>
  - <a href="sdk-for-ios-explore-structs-avoidanceoptions">AvoidanceOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidboundingboxareaoptions">AvoidBoundingBoxAreaOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidcorridorareaoptions">AvoidCorridorAreaOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidpolygonareaoptions">AvoidPolygonAreaOptions</a>
  - <a href="sdk-for-ios-explore-structs-batteryspecifications">BatterySpecifications</a>
  - <a href="sdk-for-ios-explore-structs-bicycleoptions">BicycleOptions</a>
  - <a href="sdk-for-ios-explore-structs-busoptions">BusOptions</a>
  - <a href="sdk-for-ios-explore-structs-caroptions">CarOptions</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk37CalculateIndoorRouteCompletionHandlera">CalculateIndoorRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk33CalculateIsolineCompletionHandlera">CalculateIsolineCompletionHandler</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk40CalculateTrafficOnRouteCompletionHandlera">CalculateTrafficOnRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-chargingactiondetails">ChargingActionDetails</a>
  - <a href="sdk-for-ios-explore-structs-chargingconnectorattributes">ChargingConnectorAttributes</a>
  - <a href="sdk-for-ios-explore-enums-chargingconnectortype">ChargingConnectorType</a>
  - <a href="sdk-for-ios-explore-enums-chargingconnectortype-key">– Key</a>
  - <a href="sdk-for-ios-explore-enums-chargingconnectortype-codingerror">– CodingError</a>
  - <a href="sdk-for-ios-explore-structs-chargingstation">ChargingStation</a>
  - <a href="sdk-for-ios-explore-structs-chargingstop">ChargingStop</a>
  - <a href="sdk-for-ios-explore-enums-chargingsupplytype">ChargingSupplyType</a>
  - <a href="sdk-for-ios-explore-structs-dynamicspeedinfo">DynamicSpeedInfo</a>
  - <a href="sdk-for-ios-explore-structs-electricvehicleoptions">ElectricVehicleOptions</a>
  - <a href="sdk-for-ios-explore-structs-empiricalconsumptionmodel">EmpiricalConsumptionModel</a>
  - <a href="sdk-for-ios-explore-structs-evcaroptions">EVCarOptions</a>
  - <a href="sdk-for-ios-explore-structs-evchargingpool">EVChargingPool</a>
  - <a href="sdk-for-ios-explore-structs-evchargingstation">EVChargingStation</a>
  - <a href="sdk-for-ios-explore-structs-evconsumptionmodel">EVConsumptionModel</a>
  - <a href="sdk-for-ios-explore-structs-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a>
  - <a href="sdk-for-ios-explore-structs-evtruckoptions">EVTruckOptions</a>
  - <a href="sdk-for-ios-explore-structs-fare">Fare</a>
  - <a href="sdk-for-ios-explore-structs-farepassvalidityperiod">FarePassValidityPeriod</a>
  - <a href="sdk-for-ios-explore-enums-farepassvalidityperiodtype">FarePassValidityPeriodType</a>
  - <a href="sdk-for-ios-explore-structs-fareprice">FarePrice</a>
  - <a href="sdk-for-ios-explore-enums-farepricetype">FarePriceType</a>
  - <a href="sdk-for-ios-explore-enums-farereason">FareReason</a>
  - <a href="sdk-for-ios-explore-enums-functionalroadclass">FunctionalRoadClass</a>
  - <a href="sdk-for-ios-explore-enums-hazardousmaterial">HazardousMaterial</a>
  - <a href="sdk-for-ios-explore-structs-indooravoidanceoptions">IndoorAvoidanceOptions</a>
  - <a href="sdk-for-ios-explore-classes-indoormaneuver">IndoorManeuver</a>
  - <a href="sdk-for-ios-explore-structs-indoorrouteoptions">IndoorRouteOptions</a>
  - <a href="sdk-for-ios-explore-classes-indoorroutestyle">IndoorRouteStyle</a>
  - <a href="sdk-for-ios-explore-classes-indoorroutingcontroller">IndoorRoutingController</a>
  - <a href="sdk-for-ios-explore-classes-indoorroutingengine">IndoorRoutingEngine</a>
  - <a href="sdk-for-ios-explore-enums-indoorroutingerror">IndoorRoutingError</a>
  - <a href="sdk-for-ios-explore-classes-indoorwaypoint">IndoorWaypoint</a>
  - <a href="sdk-for-ios-explore-classes-isoline">Isoline</a>
  - <a href="sdk-for-ios-explore-enums-isolinecalculationmode">IsolineCalculationMode</a>
  - <a href="sdk-for-ios-explore-structs-isolineoptions">IsolineOptions</a>
  - <a href="sdk-for-ios-explore-structs-isolineoptions-calculation">– Calculation</a>
  - <a href="sdk-for-ios-explore-enums-isolinerangetype">IsolineRangeType</a>
  - <a href="sdk-for-ios-explore-classes-isolineroutingengine">IsolineRoutingEngine</a>
  - <a href="sdk-for-ios-explore-enums-localizedtextpreference">LocalizedTextPreference</a>
  - <a href="sdk-for-ios-explore-classes-maneuver">Maneuver</a>
  - <a href="sdk-for-ios-explore-enums-maneuveraction">ManeuverAction</a>
  - <a href="sdk-for-ios-explore-structs-mapdatasize">MapDataSize</a>
  - <a href="sdk-for-ios-explore-protocols-mapdatasizelistener">MapDataSizeListener</a>
  - <a href="sdk-for-ios-explore-structs-mapmatchedcoordinates">MapMatchedCoordinates</a>
  - <a href="sdk-for-ios-explore-enums-matchsideofstreet">MatchSideOfStreet</a>
  - <a href="sdk-for-ios-explore-structs-maxaxlegroupweight">MaxAxleGroupWeight</a>
  - <a href="sdk-for-ios-explore-structs-maxspeedonsegment">MaxSpeedOnSegment</a>
  - <a href="sdk-for-ios-explore-enums-noticeseverity">NoticeSeverity</a>
  - <a href="sdk-for-ios-explore-classes-offlineroutingengine">OfflineRoutingEngine</a>
  - <a href="sdk-for-ios-explore-structs-offlineroutingengineoptions">OfflineRoutingEngineOptions</a>
  - <a href="sdk-for-ios-explore-enums-optimizationmode">OptimizationMode</a>
  - <a href="sdk-for-ios-explore-structs-passthroughwaypoint">PassThroughWaypoint</a>
  - <a href="sdk-for-ios-explore-enums-paymentmethod">PaymentMethod</a>
  - <a href="sdk-for-ios-explore-structs-pedestrianoptions">PedestrianOptions</a>
  - <a href="sdk-for-ios-explore-structs-physicalconsumptionmodel">PhysicalConsumptionModel</a>
  - <a href="sdk-for-ios-explore-classes-polygonprefetcher">PolygonPrefetcher</a>
  - <a href="sdk-for-ios-explore-structs-postaction">PostAction</a>
  - <a href="sdk-for-ios-explore-protocols-postactiondelegate">PostActionDelegate</a>
  - <a href="sdk-for-ios-explore-enums-postactiontype">PostActionType</a>
  - <a href="sdk-for-ios-explore-structs-preaction">PreAction</a>
  - <a href="sdk-for-ios-explore-enums-preactiontype">PreActionType</a>
  - <a href="sdk-for-ios-explore-protocols-prefetchstatuslistener">PrefetchStatusListener</a>
  - <a href="sdk-for-ios-explore-structs-privatebusoptions">PrivateBusOptions</a>
  - <a href="sdk-for-ios-explore-classes-refreshrouteoptions">RefreshRouteOptions</a>
  - <a href="sdk-for-ios-explore-structs-roadattributes">RoadAttributes</a>
  - <a href="sdk-for-ios-explore-protocols-roadattributesdelegate">RoadAttributesDelegate</a>
  - <a href="sdk-for-ios-explore-enums-roadfeatures">RoadFeatures</a>
  - <a href="sdk-for-ios-explore-structs-roadtexts">RoadTexts</a>
  - <a href="sdk-for-ios-explore-classes-route">Route</a>
  - <a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a>
  - <a href="sdk-for-ios-explore-structs-routelabel">RouteLabel</a>
  - <a href="sdk-for-ios-explore-enums-routelabeltype">RouteLabelType</a>
  - <a href="sdk-for-ios-explore-structs-routeoffset">RouteOffset</a>
  - <a href="sdk-for-ios-explore-structs-routeoptions">RouteOptions</a>
  - <a href="sdk-for-ios-explore-structs-routeplace">RoutePlace</a>
  - <a href="sdk-for-ios-explore-enums-routeplacedirection">RoutePlaceDirection</a>
  - <a href="sdk-for-ios-explore-enums-routeplacetype">RoutePlaceType</a>
  - <a href="sdk-for-ios-explore-classes-routeprefetcher">RoutePrefetcher</a>
  - <a href="sdk-for-ios-explore-structs-routerailwaycrossing">RouteRailwayCrossing</a>
  - <a href="sdk-for-ios-explore-enums-routerailwaycrossingtype">RouteRailwayCrossingType</a>
  - <a href="sdk-for-ios-explore-structs-routestop">RouteStop</a>
  - <a href="sdk-for-ios-explore-structs-routetextoptions">RouteTextOptions</a>
  - <a href="sdk-for-ios-explore-structs-routingconnectionsettings">RoutingConnectionSettings</a>
  - <a href="sdk-for-ios-explore-classes-routingengine">RoutingEngine</a>
  - <a href="sdk-for-ios-explore-enums-routingerror">RoutingError</a>
  - <a href="sdk-for-ios-explore-structs-routingoptions">RoutingOptions</a>
  - <a href="sdk-for-ios-explore-protocols-routingprotocol">RoutingProtocol</a>
  - <a href="sdk-for-ios-explore-structs-scooteroptions">ScooterOptions</a>
  - <a href="sdk-for-ios-explore-classes-section">Section</a>
  - <a href="sdk-for-ios-explore-structs-sectionnotice">SectionNotice</a>
  - <a href="sdk-for-ios-explore-enums-sectionnoticecode">SectionNoticeCode</a>
  - <a href="sdk-for-ios-explore-enums-sectiontransportmode">SectionTransportMode</a>
  - <a href="sdk-for-ios-explore-structs-segmentreference">SegmentReference</a>
  - <a href="sdk-for-ios-explore-enums-sideofdestination">SideOfDestination</a>
  - <a href="sdk-for-ios-explore-structs-signpost">Signpost</a>
  - <a href="sdk-for-ios-explore-structs-signpostlabel">SignpostLabel</a>
  - <a href="sdk-for-ios-explore-enums-streetattributes">StreetAttributes</a>
  - <a href="sdk-for-ios-explore-classes-span">Span</a>
  - <a href="sdk-for-ios-explore-structs-taxioptions">TaxiOptions</a>
  - <a href="sdk-for-ios-explore-structs-textusageoptions">TextUsageOptions</a>
  - <a href="sdk-for-ios-explore-structs-toll">Toll</a>
  - <a href="sdk-for-ios-explore-structs-tollfare">TollFare</a>
  - <a href="sdk-for-ios-explore-structs-tollfarepass">TollFarePass</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions">TollOptions</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions-vehiclecategory">– VehicleCategory</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions-emissiontype">– EmissionType</a>
  - <a href="sdk-for-ios-explore-structs-trafficonroute">TrafficOnRoute</a>
  - <a href="sdk-for-ios-explore-structs-trafficonspan">TrafficOnSpan</a>
  - <a href="sdk-for-ios-explore-structs-trafficonsection">TrafficOnSection</a>
  - <a href="sdk-for-ios-explore-structs-transitdeparture">TransitDeparture</a>
  - <a href="sdk-for-ios-explore-enums-transitdeparturestatus">TransitDepartureStatus</a>
  - <a href="sdk-for-ios-explore-structs-transitincident">TransitIncident</a>
  - <a href="sdk-for-ios-explore-enums-transitincidenteffect">TransitIncidentEffect</a>
  - <a href="sdk-for-ios-explore-enums-transitincidenttype">TransitIncidentType</a>
  - <a href="sdk-for-ios-explore-enums-transitmode">TransitMode</a>
  - <a href="sdk-for-ios-explore-enums-transitmodefilter">TransitModeFilter</a>
  - <a href="sdk-for-ios-explore-enums-trafficoptimizationmode">TrafficOptimizationMode</a>
  - <a href="sdk-for-ios-explore-structs-transitrouteoptions">TransitRouteOptions</a>
  - <a href="sdk-for-ios-explore-classes-transitroutingengine">TransitRoutingEngine</a>
  - <a href="sdk-for-ios-explore-structs-transitsectiondetails">TransitSectionDetails</a>
  - <a href="sdk-for-ios-explore-structs-transitstop">TransitStop</a>
  - <a href="sdk-for-ios-explore-structs-transittransport">TransitTransport</a>
  - <a href="sdk-for-ios-explore-structs-transitwaypoint">TransitWaypoint</a>
  - <a href="sdk-for-ios-explore-enums-traveldirection">TravelDirection</a>
  - <a href="sdk-for-ios-explore-structs-truckoptions">TruckOptions</a>
  - <a href="sdk-for-ios-explore-structs-truckspecifications">TruckSpecifications</a>
  - <a href="sdk-for-ios-explore-enums-trucktype">TruckType</a>
  - <a href="sdk-for-ios-explore-enums-tunnelcategory">TunnelCategory</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestrictionmaxweight">VehicleRestrictionMaxWeight</a>
  - <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype">VehicleRestrictionMaxWeightType</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification">VehicleSpecification</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-carbuilder">– CarBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-truckbuilder">– TruckBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-scooterbuilder">– ScooterBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-taxibuilder">– TaxiBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-busbuilder">– BusBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-privatebusbuilder">– PrivateBusBuilder</a>
  - <a href="sdk-for-ios-explore-structs-violatedrestriction">ViolatedRestriction</a>
  - <a href="sdk-for-ios-explore-structs-violatedrestriction-details">– Details</a>
  - <a href="sdk-for-ios-explore-enums-walkattributes">WalkAttributes</a>
  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-enums-waypointtype">WaypointType</a>
  - <a href="sdk-for-ios-explore-enums-zonecategory">ZoneCategory</a>
- <a href="sdk-for-ios-explore-navigation">Navigation</a>
  - <a href="sdk-for-ios-explore-classes-areacamerabehavior">AreaCameraBehavior</a>
  - <a href="sdk-for-ios-explore-enums-arrivalnotificationoption">ArrivalNotificationOption</a>
  - <a href="sdk-for-ios-explore-enums-aspectratio">AspectRatio</a>
  - <a href="sdk-for-ios-explore-classes-automotivecamerabehavior">AutomotiveCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-automotivecamerabehavior-orientationmode">– OrientationMode</a>
  - <a href="sdk-for-ios-explore-classes-automotivecamerabehavior-activecameratype">– ActiveCameraType</a>
  - <a href="sdk-for-ios-explore-enums-bordercrossingtype">BorderCrossingType</a>
  - <a href="sdk-for-ios-explore-structs-bordercrossingwarning">BorderCrossingWarning</a>
  - <a href="sdk-for-ios-explore-protocols-bordercrossingwarningdelegate">BorderCrossingWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-bordercrossingwarningoptions">BorderCrossingWarningOptions</a>
  - <a href="sdk-for-ios-explore-protocols-camerabehavior">CameraBehavior</a>
  - <a href="sdk-for-ios-explore-structs-currentsituationlaneview">CurrentSituationLaneView</a>
  - <a href="sdk-for-ios-explore-structs-currentsituationlaneassistanceview">CurrentSituationLaneAssistanceView</a>
  - <a href="sdk-for-ios-explore-protocols-currentsituationlaneassistanceviewdelegate">CurrentSituationLaneAssistanceViewDelegate</a>
  - <a href="sdk-for-ios-explore-structs-custompanningdata">CustomPanningData</a>
  - <a href="sdk-for-ios-explore-structs-dangerzonewarning">DangerZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-dangerzonewarningdelegate">DangerZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-destinationreacheddelegate">DestinationReachedDelegate</a>
  - <a href="sdk-for-ios-explore-structs-dimensionrestriction">DimensionRestriction</a>
  - <a href="sdk-for-ios-explore-enums-dimensionrestrictiontype">DimensionRestrictionType</a>
  - <a href="sdk-for-ios-explore-enums-directioninformationusageoption">DirectionInformationUsageOption</a>
  - <a href="sdk-for-ios-explore-enums-distancetype">DistanceType</a>
  - <a href="sdk-for-ios-explore-enums-dividermarker">DividerMarker</a>
  - <a href="sdk-for-ios-explore-classes-dynamiccamerabehavior">DynamicCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-dynamicroutingengine">DynamicRoutingEngine</a>
  - <a href="sdk-for-ios-explore-classes-dynamicroutingengine-starterror">– StartError</a>
  - <a href="sdk-for-ios-explore-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a>
  - <a href="sdk-for-ios-explore-structs-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a>
  - <a href="sdk-for-ios-explore-structs-environmentalzonewarning">EnvironmentalZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-environmentalzonewarningdelegate">EnvironmentalZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-eventtext">EventText</a>
  - <a href="sdk-for-ios-explore-protocols-eventtextdelegate">EventTextDelegate</a>
  - <a href="sdk-for-ios-explore-structs-eventtextoptions">EventTextOptions</a>
  - <a href="sdk-for-ios-explore-classes-fixedcamerabehavior">FixedCameraBehavior</a>
  - <a href="sdk-for-ios-explore-enums-generalwarningroadsigntype">GeneralWarningRoadSignType</a>
  - <a href="sdk-for-ios-explore-classes-gpxdocument">GPXDocument</a>
  - <a href="sdk-for-ios-explore-structs-gpxoptions">GPXOptions</a>
  - <a href="sdk-for-ios-explore-classes-gpxtrack">GPXTrack</a>
  - <a href="sdk-for-ios-explore-classes-gpxtrackwriter">GPXTrackWriter</a>
  - <a href="sdk-for-ios-explore-protocols-interpolatedlocationdelegate">InterpolatedLocationDelegate</a>
  - <a href="sdk-for-ios-explore-structs-junctionviewlaneassistance">JunctionViewLaneAssistance</a>
  - <a href="sdk-for-ios-explore-protocols-junctionviewlaneassistancedelegate">JunctionViewLaneAssistanceDelegate</a>
  - <a href="sdk-for-ios-explore-structs-lane">Lane</a>
  - <a href="sdk-for-ios-explore-structs-laneaccess">LaneAccess</a>
  - <a href="sdk-for-ios-explore-enums-lanedirection">LaneDirection</a>
  - <a href="sdk-for-ios-explore-structs-lanedirectioncategory">LaneDirectionCategory</a>
  - <a href="sdk-for-ios-explore-structs-lanemarkings">LaneMarkings</a>
  - <a href="sdk-for-ios-explore-enums-lanerecommendationstate">LaneRecommendationState</a>
  - <a href="sdk-for-ios-explore-structs-lanetype">LaneType</a>
  - <a href="sdk-for-ios-explore-structs-lowspeedzonewarning">LowSpeedZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-lowspeedzonewarningdelegate">LowSpeedZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-maneuvernotificationdetails">ManeuverNotificationDetails</a>
  - <a href="sdk-for-ios-explore-structs-maneuvernotificationoptions">ManeuverNotificationOptions</a>
  - <a href="sdk-for-ios-explore-structs-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a>
  - <a href="sdk-for-ios-explore-enums-maneuvernotificationtype">ManeuverNotificationType</a>
  - <a href="sdk-for-ios-explore-structs-maneuverprogress">ManeuverProgress</a>
  - <a href="sdk-for-ios-explore-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a>
  - <a href="sdk-for-ios-explore-protocols-maneuverviewlaneassistancedelegate">ManeuverViewLaneAssistanceDelegate</a>
  - <a href="sdk-for-ios-explore-structs-mapmatchedlocation">MapMatchedLocation</a>
  - <a href="sdk-for-ios-explore-structs-milestone">Milestone</a>
  - <a href="sdk-for-ios-explore-enums-milestonestatus">MilestoneStatus</a>
  - <a href="sdk-for-ios-explore-protocols-milestonestatusdelegate">MilestoneStatusDelegate</a>
  - <a href="sdk-for-ios-explore-enums-milestonetype">MilestoneType</a>
  - <a href="sdk-for-ios-explore-enums-naturalguidancetype">NaturalGuidanceType</a>
  - <a href="sdk-for-ios-explore-structs-navigablelocation">NavigableLocation</a>
  - <a href="sdk-for-ios-explore-protocols-navigablelocationdelegate">NavigableLocationDelegate</a>
  - <a href="sdk-for-ios-explore-classes-navigator">Navigator</a>
  - <a href="sdk-for-ios-explore-protocols-navigatorprotocol">NavigatorProtocol</a>
  - <a href="sdk-for-ios-explore-enums-notificationformatoption">NotificationFormatOption</a>
  - <a href="sdk-for-ios-explore-protocols-offroaddestinationreacheddelegate">OffRoadDestinationReachedDelegate</a>
  - <a href="sdk-for-ios-explore-structs-offroadprogress">OffRoadProgress</a>
  - <a href="sdk-for-ios-explore-protocols-offroadprogressdelegate">OffRoadProgressDelegate</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewrasterimage">RealisticViewRasterImage</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewvectorimage">RealisticViewVectorImage</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewwarning">RealisticViewWarning</a>
  - <a href="sdk-for-ios-explore-protocols-realisticviewwarningdelegate">RealisticViewWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewwarningoptions">RealisticViewWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-railwaycrossingwarning">RailwayCrossingWarning</a>
  - <a href="sdk-for-ios-explore-protocols-railwaycrossingwarningdelegate">RailwayCrossingWarningDelegate</a>
  - <a href="sdk-for-ios-explore-enums-roadclassification">RoadClassification</a>
  - <a href="sdk-for-ios-explore-structs-roadsign">RoadSign</a>
  - <a href="sdk-for-ios-explore-enums-roadsigncategory">RoadSignCategory</a>
  - <a href="sdk-for-ios-explore-enums-roadsigntype">RoadSignType</a>
  - <a href="sdk-for-ios-explore-structs-roadsignwarning">RoadSignWarning</a>
  - <a href="sdk-for-ios-explore-protocols-roadsignwarningdelegate">RoadSignWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-roadsignwarningoptions">RoadSignWarningOptions</a>
  - <a href="sdk-for-ios-explore-enums-roadsignvehicletype">RoadSignVehicleType</a>
  - <a href="sdk-for-ios-explore-protocols-roadtextsdelegate">RoadTextsDelegate</a>
  - <a href="sdk-for-ios-explore-structs-routedeviation">RouteDeviation</a>
  - <a href="sdk-for-ios-explore-protocols-routedeviationdelegate">RouteDeviationDelegate</a>
  - <a href="sdk-for-ios-explore-structs-routematchedlocation">RouteMatchedLocation</a>
  - <a href="sdk-for-ios-explore-structs-routeprogress">RouteProgress</a>
  - <a href="sdk-for-ios-explore-structs-routeprogresscolors">RouteProgressColors</a>
  - <a href="sdk-for-ios-explore-protocols-routeprogressdelegate">RouteProgressDelegate</a>
  - <a href="sdk-for-ios-explore-enums-safetycameratype">SafetyCameraType</a>
  - <a href="sdk-for-ios-explore-structs-safetycamerawarning">SafetyCameraWarning</a>
  - <a href="sdk-for-ios-explore-protocols-safetycamerawarningdelegate">SafetyCameraWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-safetycamerawarningoptions">SafetyCameraWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-schoolzonewarning">SchoolZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-schoolzonewarningdelegate">SchoolZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-schoolzonewarningoptions">SchoolZoneWarningOptions</a>
  - <a href="sdk-for-ios-explore-classes-sdknavigationinitializer">SDKNavigationInitializer</a>
  - <a href="sdk-for-ios-explore-structs-sectionprogress">SectionProgress</a>
  - <a href="sdk-for-ios-explore-classes-spatialaudiocuepanning">SpatialAudioCuePanning</a>
  - <a href="sdk-for-ios-explore-structs-spatialnotificationdetails">SpatialNotificationDetails</a>
  - <a href="sdk-for-ios-explore-structs-spatialtrajectorydata">SpatialTrajectoryData</a>
  - <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior">SpeedBasedCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior-profilevalue">– ProfileValue</a>
  - <a href="sdk-for-ios-explore-structs-speedlimit">SpeedLimit</a>
  - <a href="sdk-for-ios-explore-protocols-speedlimitdelegate">SpeedLimitDelegate</a>
  - <a href="sdk-for-ios-explore-structs-speedlimitoffset">SpeedLimitOffset</a>
  - <a href="sdk-for-ios-explore-protocols-speedwarningdelegate">SpeedWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-speedwarningoptions">SpeedWarningOptions</a>
  - <a href="sdk-for-ios-explore-enums-speedwarningstatus">SpeedWarningStatus</a>
  - <a href="sdk-for-ios-explore-enums-textnotificationtype">TextNotificationType</a>
  - <a href="sdk-for-ios-explore-enums-timingprofile">TimingProfile</a>
  - <a href="sdk-for-ios-explore-structs-tollbooth">TollBooth</a>
  - <a href="sdk-for-ios-explore-structs-tollboothlane">TollBoothLane</a>
  - <a href="sdk-for-ios-explore-enums-tollcollectionmethod">TollCollectionMethod</a>
  - <a href="sdk-for-ios-explore-structs-tollstop">TollStop</a>
  - <a href="sdk-for-ios-explore-protocols-tollstopwarningdelegate">TollStopWarningDelegate</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-zoompolicy">– ZoomPolicy</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-speedthreshold">– SpeedThreshold</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions">– FunctionalRoadClassZoomPolicyOptions</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-speedbasedzoompolicyoptions">– SpeedBasedZoomPolicyOptions</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverzoomrange">– ManeuverZoomRange</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverruleoptions">– ManeuverRuleOptions</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverrule">– ManeuverRule</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuvermodeconfiguration">– ManeuverModeConfiguration</a>
  - <a href="sdk-for-ios-explore-enums-trafficmergeroadtype">TrafficMergeRoadType</a>
  - <a href="sdk-for-ios-explore-enums-trafficmergeside">TrafficMergeSide</a>
  - <a href="sdk-for-ios-explore-structs-trafficmergewarning">TrafficMergeWarning</a>
  - <a href="sdk-for-ios-explore-protocols-trafficmergewarningdelegate">TrafficMergeWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-trafficmergewarningoptions">TrafficMergeWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-trafficonroutecolors">TrafficOnRouteColors</a>
  - <a href="sdk-for-ios-explore-structs-truckrestrictionwarning">TruckRestrictionWarning</a>
  - <a href="sdk-for-ios-explore-protocols-truckrestrictionswarningdelegate">TruckRestrictionsWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-truckrestrictionswarningoptions">TruckRestrictionsWarningOptions</a>
  - <a href="sdk-for-ios-explore-classes-visualnavigator">VisualNavigator</a>
  - <a href="sdk-for-ios-explore-classes-visualnavigatorcolors">VisualNavigatorColors</a>
  - <a href="sdk-for-ios-explore-protocols-wallclock">WallClock</a>
  - <a href="sdk-for-ios-explore-structs-warningnotificationdistances">WarningNotificationDistances</a>
  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>
  - <a href="sdk-for-ios-explore-enums-weathertype">WeatherType</a>
  - <a href="sdk-for-ios-explore-structs-weightrestriction">WeightRestriction</a>
  - <a href="sdk-for-ios-explore-enums-weightrestrictiontype">WeightRestrictionType</a>
- <a href="sdk-for-ios-explore-search">Search</a>
  - <a href="sdk-for-ios-explore-structs-address">Address</a>
  - <a href="sdk-for-ios-explore-enums-addresstype">AddressType</a>
  - <a href="sdk-for-ios-explore-structs-addressquery">AddressQuery</a>
  - <a href="sdk-for-ios-explore-enums-areatype">AreaType</a>
  - <a href="sdk-for-ios-explore-structs-businessdetails">BusinessDetails</a>
  - <a href="sdk-for-ios-explore-structs-categoryquery">CategoryQuery</a>
  - <a href="sdk-for-ios-explore-structs-categoryquery-area">– Area</a>
  - <a href="sdk-for-ios-explore-structs-contact">Contact</a>
  - <a href="sdk-for-ios-explore-structs-daterange">DateRange</a>
  - <a href="sdk-for-ios-explore-enums-dayofweek">DayOfWeek</a>
  - <a href="sdk-for-ios-explore-structs-details">Details</a>
  - <a href="sdk-for-ios-explore-structs-emailaddress">EmailAddress</a>
  - <a href="sdk-for-ios-explore-structs-emobilityserviceprovider">EMobilityServiceProvider</a>
  - <a href="sdk-for-ios-explore-structs-energymix">EnergyMix</a>
  - <a href="sdk-for-ios-explore-structs-energysource">EnergySource</a>
  - <a href="sdk-for-ios-explore-enums-energysourcetype">EnergySourceType</a>
  - <a href="sdk-for-ios-explore-structs-environmentalimpact">EnvironmentalImpact</a>
  - <a href="sdk-for-ios-explore-enums-environmentalimpactcategory">EnvironmentalImpactCategory</a>
  - <a href="sdk-for-ios-explore-enums-evaccessrestrictionreason">EVAccessRestrictionReason</a>
  - <a href="sdk-for-ios-explore-enums-evaccesstype">EVAccessType</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnector">EVChargingConnector</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnectorgroup">EVChargingConnectorGroup</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnectorreference">EVChargingConnectorReference</a>
  - <a href="sdk-for-ios-explore-structs-evchargingdurationrange">EVChargingDurationRange</a>
  - <a href="sdk-for-ios-explore-classes-evcharginglocation">EVChargingLocation</a>
  - <a href="sdk-for-ios-explore-enums-evcharginglocationfeature">EVChargingLocationFeature</a>
  - <a href="sdk-for-ios-explore-structs-evchargingopeninghours">EVChargingOpeningHours</a>
  - <a href="sdk-for-ios-explore-structs-evchargingopeninghoursexception">EVChargingOpeningHoursException</a>
  - <a href="sdk-for-ios-explore-structs-evchargingopeninghoursschedule">EVChargingOpeningHoursSchedule</a>
  - <a href="sdk-for-ios-explore-structs-evchargingoperator">EVChargingOperator</a>
  - <a href="sdk-for-ios-explore-structs-evchargingpooldetails">EVChargingPoolDetails</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariff">EVChargingTariff</a>
  - <a href="sdk-for-ios-explore-enums-evchargingtariffdimension">EVChargingTariffDimension</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffelement">EVChargingTariffElement</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition">EVChargingTariffElementCondition</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffpricecomponent">EVChargingTariffPriceComponent</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffrequest">EVChargingTariffRequest</a>
  - <a href="sdk-for-ios-explore-enums-evchargingtarifftype">EVChargingTariffType</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtruckrestriction">EVChargingTruckRestriction</a>
  - <a href="sdk-for-ios-explore-enums-evchargingvehiclecategory">EVChargingVehicleCategory</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk28EVCP3SearchCompletionHandlera">EVCP3SearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-evse">Evse</a>
  - <a href="sdk-for-ios-explore-classes-evsearchengine">EVSearchEngine</a>
  - <a href="sdk-for-ios-explore-enums-evsearcherror">EVSearchError</a>
  - <a href="sdk-for-ios-explore-protocols-evsearchinterface">EVSearchInterface</a>
  - <a href="sdk-for-ios-explore-structs-evsearchoptions">EVSearchOptions</a>
  - <a href="sdk-for-ios-explore-structs-evseconnector">EVSEConnector</a>
  - <a href="sdk-for-ios-explore-structs-evseinfo">EVSEInfo</a>
  - <a href="sdk-for-ios-explore-enums-evsestatus">EVSEStatus</a>
  - <a href="sdk-for-ios-explore-enums-facilitytype">FacilityType</a>
  - <a href="sdk-for-ios-explore-structs-fueladditive">FuelAdditive</a>
  - <a href="sdk-for-ios-explore-enums-fueladditivetype">FuelAdditiveType</a>
  - <a href="sdk-for-ios-explore-structs-fuelstation">FuelStation</a>
  - <a href="sdk-for-ios-explore-enums-fueltype">FuelType</a>
  - <a href="sdk-for-ios-explore-structs-genericfuel">GenericFuel</a>
  - <a href="sdk-for-ios-explore-structs-geoplace">GeoPlace</a>
  - <a href="sdk-for-ios-explore-enums-highlighttype">HighlightType</a>
  - <a href="sdk-for-ios-explore-classes-indexrange">IndexRange</a>
  - <a href="sdk-for-ios-explore-structs-landlinephone">LandlinePhone</a>
  - <a href="sdk-for-ios-explore-structs-locationdetails">LocationDetails</a>
  - <a href="sdk-for-ios-explore-structs-mobilephone">MobilePhone</a>
  - <a href="sdk-for-ios-explore-classes-myplaces">MyPlaces</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchengine">OfflineSearchEngine</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex">OfflineSearchIndex</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex-operation">– Operation</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex-error">– Error</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex-options">– Options</a>
  - <a href="sdk-for-ios-explore-protocols-offlinesearchindexlistener">OfflineSearchIndexListener</a>
  - <a href="sdk-for-ios-explore-structs-openinghours">OpeningHours</a>
  - <a href="sdk-for-ios-explore-enums-parkingtype">ParkingType</a>
  - <a href="sdk-for-ios-explore-classes-place">Place</a>
  - <a href="sdk-for-ios-explore-classes-placecategory">PlaceCategory</a>
  - <a href="sdk-for-ios-explore-structs-placechain">PlaceChain</a>
  - <a href="sdk-for-ios-explore-structs-placefilter">PlaceFilter</a>
  - <a href="sdk-for-ios-explore-structs-placefilter-ev">– Ev</a>
  - <a href="sdk-for-ios-explore-structs-placefoodtype">PlaceFoodType</a>
  - <a href="sdk-for-ios-explore-structs-placeidquery">PlaceIdQuery</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera">PlaceIdSearchExtendedCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-placeserializationerror">PlaceSerializationError</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk27PlaceSerializationExceptiona">PlaceSerializationException</a>
  - <a href="sdk-for-ios-explore-enums-placetype">PlaceType</a>
  - <a href="sdk-for-ios-explore-structs-poipaymentdetails">POIPaymentDetails</a>
  - <a href="sdk-for-ios-explore-structs-poipaymentmethod">POIPaymentMethod</a>
  - <a href="sdk-for-ios-explore-structs-responsedetails">ResponseDetails</a>
  - <a href="sdk-for-ios-explore-structs-scheduledetails">ScheduleDetails</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a>
  - <a href="sdk-for-ios-explore-classes-searchengine">SearchEngine</a>
  - <a href="sdk-for-ios-explore-enums-searcherror">SearchError</a>
  - <a href="sdk-for-ios-explore-protocols-searchinterface">SearchInterface</a>
  - <a href="sdk-for-ios-explore-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-explore-structs-structuredquery">StructuredQuery</a>
  - <a href="sdk-for-ios-explore-structs-structuredquery-resulttype">– ResultType</a>
  - <a href="sdk-for-ios-explore-structs-structuredquery-addresselements">– AddressElements</a>
  - <a href="sdk-for-ios-explore-classes-suggestion">Suggestion</a>
  - <a href="sdk-for-ios-explore-enums-suggestiontype">SuggestionType</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk32SuggestExtendedCompletionHandlera">SuggestExtendedCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-supplierreference">SupplierReference</a>
  - <a href="sdk-for-ios-explore-structs-textquery">TextQuery</a>
  - <a href="sdk-for-ios-explore-structs-textquery-area">– Area</a>
  - <a href="sdk-for-ios-explore-structs-timeofdayrange">TimeOfDayRange</a>
  - <a href="sdk-for-ios-explore-structs-truckamenities">TruckAmenities</a>
  - <a href="sdk-for-ios-explore-structs-truckfuel">TruckFuel</a>
  - <a href="sdk-for-ios-explore-structs-webdetails">WebDetails</a>
  - <a href="sdk-for-ios-explore-structs-webeditorial">WebEditorial</a>
  - <a href="sdk-for-ios-explore-structs-webimage">WebImage</a>
  - <a href="sdk-for-ios-explore-structs-webrating">WebRating</a>
  - <a href="sdk-for-ios-explore-structs-websiteaddress">WebsiteAddress</a>
  - <a href="sdk-for-ios-explore-structs-websource">WebSource</a>
  - <a href="sdk-for-ios-explore-classes-w3wsearchengine">W3WSearchEngine</a>
  - <a href="sdk-for-ios-explore-enums-w3wsearcherror">W3WSearchError</a>
  - <a href="sdk-for-ios-explore-structs-w3wsquare">W3WSquare</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk26W3WSearchCompletionHandlera">W3WSearchCompletionHandler</a>
- <a href="sdk-for-ios-explore-traffic">Traffic</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a>
  - <a href="sdk-for-ios-explore-classes-trafficengine">TrafficEngine</a>
  - <a href="sdk-for-ios-explore-classes-trafficflow">TrafficFlow</a>
  - <a href="sdk-for-ios-explore-protocols-trafficflowbase">TrafficFlowBase</a>
  - <a href="sdk-for-ios-explore-structs-trafficflowqueryoptions">TrafficFlowQueryOptions</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-classes-trafficincident">TrafficIncident</a>
  - <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory">– RestrictedVehicleCategory</a>
  - <a href="sdk-for-ios-explore-classes-trafficincident-vehiclerestriction">– VehicleRestriction</a>
  - <a href="sdk-for-ios-explore-protocols-trafficincidentbase">TrafficIncidentBase</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk32TrafficIncidentCompletionHandlera">TrafficIncidentCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-trafficincidentimpact">TrafficIncidentImpact</a>
  - <a href="sdk-for-ios-explore-structs-trafficincidentlookupoptions">TrafficIncidentLookupOptions</a>
  - <a href="sdk-for-ios-explore-classes-trafficincidentonroute">TrafficIncidentOnRoute</a>
  - <a href="sdk-for-ios-explore-enums-trafficincidenttype">TrafficIncidentType</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a>
  - <a href="sdk-for-ios-explore-structs-trafficlocation">TrafficLocation</a>
  - <a href="sdk-for-ios-explore-enums-trafficqueryerror">TrafficQueryError</a>
  - <a href="sdk-for-ios-explore-enums-traversability">Traversability</a>
- <a href="sdk-for-ios-explore-trafficradio">TrafficRadio</a>
  - <a href="sdk-for-ios-explore-classes-trafficbroadcast">TrafficBroadcast</a>
  - <a href="sdk-for-ios-explore-structs-trafficbroadcastparameters">TrafficBroadcastParameters</a>
  - <a href="sdk-for-ios-explore-structs-tmcdata">TMCData</a>
  - <a href="sdk-for-ios-explore-structs-tmcpreferredsidsrequest">TMCPreferredSidsRequest</a>
  - <a href="sdk-for-ios-explore-structs-tmcserviceproviderinfo">TMCServiceProviderInfo</a>
  - <a href="sdk-for-ios-explore-structs-tmcservicerequest">TMCServiceRequest</a>
  - <a href="sdk-for-ios-explore-protocols-tmcserviceinterface">TMCServiceInterface</a>
  - <a href="sdk-for-ios-explore-structs-rdsencryptionkey">RDSEncryptionKey</a>
  - <a href="sdk-for-ios-explore-structs-rdsencryptionkeysrequest">RDSEncryptionKeysRequest</a>
- <a href="sdk-for-ios-explore-transport">Transport</a>
  - <a href="sdk-for-ios-explore-structs-busspecifications">BusSpecifications</a>
  - <a href="sdk-for-ios-explore-structs-carspecifications">CarSpecifications</a>
  - <a href="sdk-for-ios-explore-structs-generalvehiclespeedlimits">GeneralVehicleSpeedLimits</a>
  - <a href="sdk-for-ios-explore-structs-hazardousmaterialrestriction">HazardousMaterialRestriction</a>
  - <a href="sdk-for-ios-explore-structs-pedestrianspecification">PedestrianSpecification</a>
  - <a href="sdk-for-ios-explore-enums-restrictiontype">RestrictionType</a>
  - <a href="sdk-for-ios-explore-structs-scooterspecification">ScooterSpecification</a>
  - <a href="sdk-for-ios-explore-structs-specificrestriction">SpecificRestriction</a>
  - <a href="sdk-for-ios-explore-structs-taxispecification">TaxiSpecification</a>
  - <a href="sdk-for-ios-explore-structs-timerestriction">TimeRestriction</a>
  - <a href="sdk-for-ios-explore-structs-timerestriction-category">– Category</a>
  - <a href="sdk-for-ios-explore-enums-transportmode">TransportMode</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification">TransportSpecification</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-carbuilder">– CarBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-truckbuilder">– TruckBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-pedestrianbuilder">– PedestrianBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-scooterbuilder">– ScooterBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-bicyclebuilder">– BicycleBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-taxibuilder">– TaxiBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-busbuilder">– BusBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-privatebusbuilder">– PrivateBusBuilder</a>
  - <a href="sdk-for-ios-explore-enums-transporttype">TransportType</a>
  - <a href="sdk-for-ios-explore-enums-truckcategory">TruckCategory</a>
  - <a href="sdk-for-ios-explore-enums-truckclass">TruckClass</a>
  - <a href="sdk-for-ios-explore-enums-truckroadtype">TruckRoadType</a>
  - <a href="sdk-for-ios-explore-enums-truckfueltype">TruckFuelType</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestriction">VehicleRestriction</a>
  - <a href="sdk-for-ios-explore-enums-vehicletype">VehicleType</a>
  - <a href="sdk-for-ios-explore-structs-vehicleprofile">VehicleProfile</a>
  - <a href="sdk-for-ios-explore-structs-weightperaxlegroup">WeightPerAxleGroup</a>
- <a href="sdk-for-ios-explore-venues">Venues</a>
  - <a href="sdk-for-ios-explore-classes-crosswalk">Crosswalk</a>
  - <a href="sdk-for-ios-explore-classes-crosswalk-classificationstyle">– ClassificationStyle</a>
  - <a href="sdk-for-ios-explore-classes-property">Property</a>
  - <a href="sdk-for-ios-explore-classes-property-propertytype">– PropertyType</a>
  - <a href="sdk-for-ios-explore-classes-venue">Venue</a>
  - <a href="sdk-for-ios-explore-protocols-venuedelegate">VenueDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venuedrawing">VenueDrawing</a>
  - <a href="sdk-for-ios-explore-protocols-venuedrawingselectiondelegate">VenueDrawingSelectionDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venueengine">VenueEngine</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk32VenueEngineInitCompletionHandlera">VenueEngineInitCompletionHandler</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk10VenueErrora">VenueError</a>
  - <a href="sdk-for-ios-explore-enums-venueerrorcode">VenueErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry">VenueGeometry</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry-internaladdress">– InternalAddress</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry-geometrytype">– GeometryType</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry-lookuptype">– LookupType</a>
  - <a href="sdk-for-ios-explore-enums-venuegeometryfiltertype">VenueGeometryFilterType</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometrystyle">VenueGeometryStyle</a>
  - <a href="sdk-for-ios-explore-classes-venueinfo">VenueInfo</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk17VenueInfoDataLista">VenueInfoDataList</a>
  - <a href="sdk-for-ios-explore-protocols-venueinfolistlistenerdelegate">VenueInfoListListenerDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venuelabelstyle">VenueLabelStyle</a>
  - <a href="sdk-for-ios-explore-classes-venuelevel">VenueLevel</a>
  - <a href="sdk-for-ios-explore-protocols-venuelevelselectiondelegate">VenueLevelSelectionDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-venuelifecycledelegate">VenueLifecycleDelegate</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a>
  - <a href="sdk-for-ios-explore-classes-venuemap">VenueMap</a>
  - <a href="sdk-for-ios-explore-protocols-venuemapdelegate">VenueMapDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-venuemaplifecycledelegate">VenueMapLifecycleDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venuemodel">VenueModel</a>
  - <a href="sdk-for-ios-explore-protocols-venueselectiondelegate">VenueSelectionDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venueservice">VenueService</a>
  - <a href="sdk-for-ios-explore-classes-venueservice-venueoptionalfeature">– VenueOptionalFeature</a>
  - <a href="sdk-for-ios-explore-protocols-venueservicedelegate">VenueServiceDelegate</a>
  - <a href="sdk-for-ios-explore-enums-venueserviceinitstatus">VenueServiceInitStatus</a>
  - <a href="sdk-for-ios-explore-classes-venuestyle">VenueStyle</a>
  - <a href="sdk-for-ios-explore-classes-venuetopology">VenueTopology</a>
  - <a href="sdk-for-ios-explore-classes-venuetopology-accesscharacteristics">– AccessCharacteristics</a>
  - <a href="sdk-for-ios-explore-classes-venuetopology-topologydirectionality">– TopologyDirectionality</a>
  - <a href="sdk-for-ios-explore-enums-venuetransportmode">VenueTransportMode</a>
  - <a href="sdk-for-ios-explore-enums-venuetransportmode-key">– Key</a>
  - <a href="sdk-for-ios-explore-enums-venuetransportmode-codingerror">– CodingError</a>
- <a href="sdk-for-ios-explore-warnerengine">WarnerEngine</a>
  - <a href="sdk-for-ios-explore-structs-customwarning">CustomWarning</a>
  - <a href="sdk-for-ios-explore-protocols-customwarningprovider">CustomWarningProvider</a>
  - <a href="sdk-for-ios-explore-structs-warning">Warning</a>
  - <a href="sdk-for-ios-explore-classes-warnerengine">WarnerEngine</a>
  - <a href="sdk-for-ios-explore-protocols-warningdelegate">WarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-warningoptions">WarningOptions</a>
  - <a href="sdk-for-ios-explore-classes-warningsregistry">WarningsRegistry</a>
- <a href="sdk-for-ios-explore-other%20classes">Other Classes</a>
  - <a href="sdk-for-ios-explore-classes-indoorsectiondetails">IndoorSectionDetails</a>
  - <a href="sdk-for-ios-explore-classes-locationmanager">LocationManager</a>
- <a href="sdk-for-ios-explore-other%20enums">Other Enumerations</a>
  - <a href="sdk-for-ios-explore-enums-commercialvehicleroadtype">CommercialVehicleRoadType</a>
  - <a href="sdk-for-ios-explore-enums-hazardousmaterialtype">HazardousMaterialType</a>
  - <a href="sdk-for-ios-explore-enums-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a>
  - <a href="sdk-for-ios-explore-enums-indoormaneuveractions">IndoorManeuverActions</a>
  - <a href="sdk-for-ios-explore-enums-physicalstructure">PhysicalStructure</a>
  - <a href="sdk-for-ios-explore-enums-vehicletypecondition">VehicleTypeCondition</a>
- <a href="sdk-for-ios-explore-other%20functions">Other Functions</a>
  - <a href="sdk-for-ios-explore-other%20functions#/s:7heresdk24makeIOSPlatformThreadingAA08PlatformD0_pyF">makeIOSPlatformThreading()</a>
  - <a href="sdk-for-ios-explore-other%20functions#/s:7heresdk12synchronized_7closurexyp_xyXEtlF">synchronized(\_:closure:)</a>
- <a href="sdk-for-ios-explore-other%20protocols">Other Protocols</a>
  - <a href="sdk-for-ios-explore-protocols-matchedlocationlistener">MatchedLocationListener</a>
- <a href="sdk-for-ios-explore-other%20structs">Other Structures</a>
  - <a href="sdk-for-ios-explore-structs-admincontextid">AdminContextId</a>
  - <a href="sdk-for-ios-explore-structs-administrativecommercialvehiclerules">AdministrativeCommercialVehicleRules</a>
  - <a href="sdk-for-ios-explore-structs-driverestregulation">DriveRestRegulation</a>
  - <a href="sdk-for-ios-explore-structs-indoorlevelchangedata">IndoorLevelChangeData</a>
  - <a href="sdk-for-ios-explore-structs-indoorrouteplace">IndoorRoutePlace</a>
  - <a href="sdk-for-ios-explore-structs-indoorspacedata">IndoorSpaceData</a>
  - <a href="sdk-for-ios-explore-structs-lanedecreasewarning">LaneDecreaseWarning</a>
  - <a href="sdk-for-ios-explore-structs-lanedecreasewarningoptions">LaneDecreaseWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-refreshrouteparameters">RefreshRouteParameters</a>
  - <a href="sdk-for-ios-explore-structs-roadprofilecondition">RoadProfileCondition</a>
  - <a href="sdk-for-ios-explore-structs-vehicleprofilerestriction">VehicleProfileRestriction</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestrictioncondition">VehicleRestrictionCondition</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecificaccess">VehicleSpecificAccess</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecificspeedlimit">VehicleSpecificSpeedLimit</a>

</nav>

<article class="main-content">

<div class="section">

<div class="section section">

# Core

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk8Anchor2DV"></span>` `<span id="//apple_ref/swift/Struct/Anchor2D" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8Anchor2DV" class="token"><code>Anchor2D</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a point in a rectangle as a ratio of this rectangle’s width and height.

  <a href="sdk-for-ios-explore-structs-anchor2d" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Anchor2D : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16Anchor2DKeyframeV"></span>` `<span id="//apple_ref/swift/Struct/Anchor2DKeyframe" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk16Anchor2DKeyframeV" class="token"><code>Anchor2DKeyframe</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An Anchor2D keyframe. A keyframe consists of a value and an animation duration.

  <a href="sdk-for-ios-explore-structs-anchor2dkeyframe" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Anchor2DKeyframe : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5AngleC"></span>` `<span id="//apple_ref/swift/Class/Angle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk5AngleC" class="token"><code>Angle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents an angle independent of the unit of measurement.

  <a href="sdk-for-ios-explore-classes-angle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Angle
  ```

  ``` highlight
  extension Angle: NativeBase
  ```

  ``` highlight
  extension Angle: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10AngleRangeV"></span>` `<span id="//apple_ref/swift/Struct/AngleRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10AngleRangeV" class="token"><code>AngleRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents angle ranges as a circular sector by using an absolute start angle and a relative range angle called extent. They both define a sector on a circle. All angles are in degrees and are clockwise-oriented. By default, the AngleRange represents the entire circle, the value is in the range of \[0, 360\]. Values will be corrected during construction using normalization for the start angle and clamping for the extent angle, ensuring a valid range for all possible inputs.

  <a href="sdk-for-ios-explore-structs-anglerange" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct AngleRange : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14AuthenticationC"></span>` `<span id="//apple_ref/swift/Class/Authentication" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14AuthenticationC" class="token"><code>Authentication</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use the authentication class to authenticate and retrieve a secure token that can be used with other HERE services.

  <a href="sdk-for-ios-explore-classes-authentication" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Authentication
  ```

  ``` highlight
  extension Authentication: NativeBase
  ```

  ``` highlight
  extension Authentication: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk31AuthenticationCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/AuthenticationCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk31AuthenticationCompletionHandlera" class="token"><code>AuthenticationCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol passed to

      Authentication.authenticate(SDKNativeEngine)

  . This protocol is called on the main thread asynchronously when an authenticate call has completed.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias AuthenticationCompletionHandler = ( _ authenticationError : AuthenticationError ?, _ authenticationData : AuthenticationData ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>authenticationError</code></em><code> </code></td>
  <td><div>
  <p>Represents the operation status. It is ‘null’ for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>authenticationData</code></em><code> </code></td>
  <td><div>
  <p>Represents the authentication data.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23AuthenticationExceptiona"></span>` `<span id="//apple_ref/swift/Alias/AuthenticationException" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk23AuthenticationExceptiona" class="token"><code>AuthenticationException</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authentication exception

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias AuthenticationException = AuthenticationError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18AuthenticationModeC"></span>` `<span id="//apple_ref/swift/Class/AuthenticationMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18AuthenticationModeC" class="token"><code>AuthenticationMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This is a bearer authentication mode which adds or does not add a header (“Authorization”, “Bearer \$Token”) to each online request of the module the object is added to. The token (if used) can be provided or is retrieved via key/secret from a dedicated backend.

  <a href="sdk-for-ios-explore-classes-authenticationmode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class AuthenticationMode
  ```

  ``` highlight
  extension AuthenticationMode: NativeBase
  ```

  ``` highlight
  extension AuthenticationMode: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9BrandLogoV"></span>` `<span id="//apple_ref/swift/Struct/BrandLogo" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9BrandLogoV" class="token"><code>BrandLogo</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents image link to the company’s logo. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-brandlogo" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct BrandLogo : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30CacheCallbackCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/CacheCallbackCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk30CacheCallbackCompletionHandlera" class="token"><code>CacheCallbackCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when

      SDKCache.clearCache(...)

  has been completed.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias CacheCallbackCompletionHandler = ( _ maploaderError : MapLoaderError ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>maploaderError</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds. Please note, in case of failure, only <a href="sdk-for-ios-explore-enums-maploadererror#/s:7heresdk14MapLoaderErrorO08internalD0yA2CmF"><code>MapLoaderError.internalError</code></a> error returned for now.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17CardinalDirectionO"></span>` `<span id="//apple_ref/swift/Enum/CardinalDirection" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk17CardinalDirectionO" class="token"><code>CardinalDirection</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the official directional identifier assigned to this road. The direction indicates the same information as on the signpost shield text: For example, if it is “101 West”, the direction contains WEST.

  <a href="sdk-for-ios-explore-enums-cardinaldirection" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum CardinalDirection : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20CatalogConfigurationV"></span>` `<span id="//apple_ref/swift/Struct/CatalogConfiguration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk20CatalogConfigurationV" class="token"><code>CatalogConfiguration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Using this class you can configure in the <a href="sdk-for-ios-explore-structs-sdkoptions">`SDKOptions`</a>, how the <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a> should access, use and store the data for the desired catalog.

  Using this class, you can access default catalogs on the HERE platform and also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases.

  For information on how the user can identify a catalog on the HERE platform, see <a href="sdk-for-ios-explore-structs-desiredcatalog">`DesiredCatalog`</a> For further information about catalogs and related concepts see <a href="sdk-for-ios-explore-structs-catalogidentifier">`CatalogIdentifier`</a>.

  **Note:** This API is only applicable for the Navigate license.

  <a href="sdk-for-ios-explore-structs-catalogconfiguration" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CatalogConfiguration : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17CatalogIdentifierV"></span>` `<span id="//apple_ref/swift/Struct/CatalogIdentifier" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk17CatalogIdentifierV" class="token"><code>CatalogIdentifier</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class is used to identify any catalog in the HERE platform.

  A catalog is a storage-representation to store map data on the HERE platform. The data inside a catalog is divided into layers, where each layer consists of datasets with similar functional attributes in the physical world. For example, there can be a layer for road-topology, a layer for road-attributes (such as speed limits) and a layer for places and business addresses. All these layers, in different geographic regions, can be grouped together into a catalog to create a representation of the world we live in, called HERE map. It can be also used to render a <a href="sdk-for-ios-explore-classes-mapview">`MapView`</a>. Each geographic region is cut into geospatial tiles for efficient search, map display, routing, map matching, and driver warnings. Each tile partitions the map data (in one or more layers, depending on the product) in the geolocation of that specific tile. The data inside a catalog is logically managed and access controlled as a single set. If you have any data that you want to bring to the HERE platform, you need a catalog to contain it. For additional information about catalogs, and related concepts of data representation on the HERE platform, refer to <a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/catalogs.html">the Data API</a> and <a href="https://www.here.com/docs/bundle/introduction-to-mapping-concepts-user-guide/page/topics/maps-layers-tiles.html">Introduction to Mapping Concepts</a>

  <a href="sdk-for-ios-explore-structs-catalogidentifier" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CatalogIdentifier : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11CatalogTypeO"></span>` `<span id="//apple_ref/swift/Enum/CatalogType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11CatalogTypeO" class="token"><code>CatalogType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents default HERE catalog types.

  <a href="sdk-for-ios-explore-enums-catalogtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum CatalogType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17CatalogUpdateTaskC"></span>` `<span id="//apple_ref/swift/Class/CatalogUpdateTask" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk17CatalogUpdateTaskC" class="token"><code>CatalogUpdateTask</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class to control the catalog update process.

  <a href="sdk-for-ios-explore-classes-catalogupdatetask" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class CatalogUpdateTask
  ```

  ``` highlight
  extension CatalogUpdateTask: NativeBase
  ```

  ``` highlight
  extension CatalogUpdateTask: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18CatalogVersionHintC"></span>` `<span id="//apple_ref/swift/Class/CatalogVersionHint" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18CatalogVersionHintC" class="token"><code>CatalogVersionHint</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This is a class for capturing user’s intent for the desired catalog version to use in <a href="sdk-for-ios-explore-structs-desiredcatalog">`DesiredCatalog`</a> class.

  You can request a specific or latest version of a catalog by calling the static functions

      CatalogVersionHint.specific(...)

  and
      CatalogVersionHint.latest(...)

  respectively. The HERE platform will make the best effort to provide an appropriate version for the catalog based on this version hint. Please take note that for the API
      CatalogVersionHint.specific(...)

  to function properly, it is essential that the mutable and persistent storage should be cleaned.
  </p>

  <a href="sdk-for-ios-explore-classes-catalogversionhint" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class CatalogVersionHint
  ```

  ``` highlight
  extension CatalogVersionHint: NativeBase
  ```

  ``` highlight
  extension CatalogVersionHint: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12CollectionOfC"></span>` `<span id="//apple_ref/swift/Class/CollectionOf" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk12CollectionOfC" class="token"><code>CollectionOf</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Custom collection implementation.

  <a href="sdk-for-ios-explore-classes-collectionof" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class CollectionOf<T> : Collection
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11CountryCodeO"></span>` `<span id="//apple_ref/swift/Enum/CountryCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11CountryCodeO" class="token"><code>CountryCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum represents country codes in accordance with the ISO 3166-1 standard using alpha-3 codes.

  <a href="sdk-for-ios-explore-enums-countrycode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum CountryCode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11CurrentTypeO"></span>` `<span id="//apple_ref/swift/Enum/CurrentType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11CurrentTypeO" class="token"><code>CurrentType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum represents the type of electric current

  <a href="sdk-for-ios-explore-enums-currenttype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum CurrentType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19CustomMetadataValueP"></span>` `<span id="//apple_ref/swift/Protocol/CustomMetadataValue" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk19CustomMetadataValueP" class="token"><code>CustomMetadataValue</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for storing arbitrary metadata types. By implementing this protocol, multiple object types can be stored as desired, simply by adding fields to the implementation that refer to those objects and then assigning an instance of the CustomMetadataValue derived class to a map item.

  <a href="sdk-for-ios-explore-protocols-custommetadatavalue" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol CustomMetadataValue : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14DesiredCatalogV"></span>` `<span id="//apple_ref/swift/Struct/DesiredCatalog" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14DesiredCatalogV" class="token"><code>DesiredCatalog</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access. The user can specify the HERE Resource Name (HRN) for the catalog along with a hint for the desired version. If the desired version is not available, the HERE platform will determine the best version to use for a specific catalog or result in error logs. For information on how to specify the catalog version, see <a href="sdk-for-ios-explore-classes-catalogversionhint">`CatalogVersionHint`</a>. For information about catalogs and related concepts see <a href="sdk-for-ios-explore-structs-catalogidentifier">`CatalogIdentifier`</a>.

  <a href="sdk-for-ios-explore-structs-desiredcatalog" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct DesiredCatalog : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14DeviceIdHandlea"></span>` `<span id="//apple_ref/swift/Alias/DeviceIdHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14DeviceIdHandlea" class="token"><code>DeviceIdHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method will be called on the main thread when

      SDKNativeEngine.getDeviceId(...)

  has been completed.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias DeviceIdHandle = ( _ deviceId : String ) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>deviceId</code></em><code> </code></td>
  <td><div>
  <p>Represents a deviceId, a unique identifier assigned to the device for this application.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EngineBaseURLO"></span>` `<span id="//apple_ref/swift/Enum/EngineBaseURL" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk13EngineBaseURLO" class="token"><code>EngineBaseURL</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.

  <a href="sdk-for-ios-explore-enums-enginebaseurl" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EngineBaseURL : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EngineOptionsV"></span>` `<span id="//apple_ref/swift/Struct/EngineOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk13EngineOptionsV" class="token"><code>EngineOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies several options specific to different engines. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-engineoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EngineOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10ExternalIDV"></span>` `<span id="//apple_ref/swift/Struct/ExternalID" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10ExternalIDV" class="token"><code>ExternalID</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier of the entity as provided by the external source

  <a href="sdk-for-ios-explore-structs-externalid" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ExternalID : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk6GeoBoxV"></span>` `<span id="//apple_ref/swift/Struct/GeoBox" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk6GeoBoxV" class="token"><code>GeoBox</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a bounding rectangle aligned with latitude and longitude. Geographic area represented by this would be visualised as a rectangle when using a normal cylindrical projection (such as Mercator). The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction. The box with equal values in longitude for the corners is considered as a span of 360 degrees. The box is considered empty if the latitude of the <a href="sdk-for-ios-explore-structs-geobox#/s:7heresdk6GeoBoxV15southWestCornerAA0B11CoordinatesVvp">`GeoBox.southWestCorner`</a> is larger than the the latitude of the <a href="sdk-for-ios-explore-structs-geobox#/s:7heresdk6GeoBoxV15northEastCornerAA0B11CoordinatesVvp">`GeoBox.northEastCorner`</a>.

  <a href="sdk-for-ios-explore-structs-geobox" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoBox : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9GeoCircleV"></span>` `<span id="//apple_ref/swift/Struct/GeoCircle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9GeoCircleV" class="token"><code>GeoCircle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a circle area in 2D space.

  <a href="sdk-for-ios-explore-structs-geocircle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoCircle : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14GeoCoordinatesV"></span>` `<span id="//apple_ref/swift/Struct/GeoCoordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14GeoCoordinatesV" class="token"><code>GeoCoordinates</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents geographical coordinates in 3D space.

  <a href="sdk-for-ios-explore-structs-geocoordinates" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoCoordinates : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20GeoCoordinatesUpdateV"></span>` `<span id="//apple_ref/swift/Struct/GeoCoordinatesUpdate" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk20GeoCoordinatesUpdateV" class="token"><code>GeoCoordinatesUpdate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents geographical coordinates in 3D space. Unlike <a href="sdk-for-ios-explore-structs-geocoordinates">`GeoCoordinates`</a>, its members can be undefined, allowing for APIs that update only the specified parts of geo coordinates.

  <a href="sdk-for-ios-explore-structs-geocoordinatesupdate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoCoordinatesUpdate : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11GeoCorridorV"></span>` `<span id="//apple_ref/swift/Struct/GeoCorridor" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11GeoCorridorV" class="token"><code>GeoCorridor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A geographical area that wraps around a geographical polyline with a given distance. The corridor has round edges at the endpoints of the polyline. The distance from any point of the polyline to the closest border of the corridor is always the same.

  <a href="sdk-for-ios-explore-structs-geocorridor" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoCorridor : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14GeoOrientationV"></span>` `<span id="//apple_ref/swift/Struct/GeoOrientation" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14GeoOrientationV" class="token"><code>GeoOrientation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geodetic orientation with bearing, tilt and roll.

  <a href="sdk-for-ios-explore-structs-geoorientation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoOrientation : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20GeoOrientationUpdateV"></span>` `<span id="//apple_ref/swift/Struct/GeoOrientationUpdate" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk20GeoOrientationUpdateV" class="token"><code>GeoOrientationUpdate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes geodetic orientation update with bearing and tilt. Updating an orientation value can be skipped by setting `nil` in an appriopriate field. For example, if one wants bearing not to be updated set it to `nil`.

  <a href="sdk-for-ios-explore-structs-geoorientationupdate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoOrientationUpdate : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10GeoPolygonV"></span>` `<span id="//apple_ref/swift/Struct/GeoPolygon" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10GeoPolygonV" class="token"><code>GeoPolygon</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a `GeoPolygon` area as a series of geographic coordinates, and optionally, a list of inner boundaries (also known as holes). An instance of this class, initialized with appropriate vertices.

  <a href="sdk-for-ios-explore-structs-geopolygon" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoPolygon : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11GeoPolylineV"></span>` `<span id="//apple_ref/swift/Struct/GeoPolyline" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11GeoPolylineV" class="token"><code>GeoPolyline</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A list of geographic coordinates representing the vertices of a polyline. An instance of this class, initialized with appropriate vertices. Represents a `GeoPolyline` as a series of geographic coordinates.

  <a href="sdk-for-ios-explore-structs-geopolyline" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoPolyline : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20GeoPolylineDirectionO"></span>` `<span id="//apple_ref/swift/Enum/GeoPolylineDirection" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk20GeoPolylineDirectionO" class="token"><code>GeoPolylineDirection</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines if a function on a <a href="sdk-for-ios-explore-structs-geopolyline">`GeoPolyline`</a> computes the operation starting from the beginning or from the end of <a href="sdk-for-ios-explore-structs-geopolyline#/s:7heresdk11GeoPolylineV8verticesSayAA0B11CoordinatesVGvp">`GeoPolyline.vertices`</a>.

  <a href="sdk-for-ios-explore-enums-geopolylinedirection" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum GeoPolylineDirection : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18InstantiationErrora"></span>` `<span id="//apple_ref/swift/Alias/InstantiationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18InstantiationErrora" class="token"><code>InstantiationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Instantiation error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias InstantiationError = InstantiationErrorCode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/InstantiationErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Instantiation error.

  <a href="sdk-for-ios-explore-enums-instantiationerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension InstantiationErrorCode : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12IntegerRangeV"></span>` `<span id="//apple_ref/swift/Struct/IntegerRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk12IntegerRangeV" class="token"><code>IntegerRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An integer range \[min, max\] with inclusive minimum and maximum value.

  <a href="sdk-for-ios-explore-structs-integerrange" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct IntegerRange : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23JunctionsTraversabilityO"></span>` `<span id="//apple_ref/swift/Enum/JunctionsTraversability" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk23JunctionsTraversabilityO" class="token"><code>JunctionsTraversability</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Junctions traversability of some traffic incident or flow section.

  <a href="sdk-for-ios-explore-enums-junctionstraversability" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum JunctionsTraversability : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12LanguageCodeO"></span>` `<span id="//apple_ref/swift/Enum/LanguageCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk12LanguageCodeO" class="token"><code>LanguageCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum represents language codes. The basic naming pattern consists of a 2-letter ISO 639-1 language code followed by a 2-letter ISO 3166-1 country code. Some language codes consist only of a language code, i.e. without a country code. When there is no ISO 639-1 language code, the related ISO 639-2 or ISO 639-3 language code is used. In case the script is specified, its ISO 15924 code is used.

  <a href="sdk-for-ios-explore-enums-languagecode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LanguageCode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18LayerConfigurationV"></span>` `<span id="//apple_ref/swift/Struct/LayerConfiguration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18LayerConfigurationV" class="token"><code>LayerConfiguration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class to configure which layers should be enabled or disabled in the OCM map data. Disabling a layer allows to reduce the amount of data that will be downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.

  `LayerConfiguration` changes made via <a href="sdk-for-ios-explore-structs-sdkoptions">`SDKOptions`</a> require `sdk.maploader.MapUpdater` to align previously downloaded content. To ensure that the changes in <a href="sdk-for-ios-explore-structs-sdkoptions">`SDKOptions`</a> affect the map data, it is recommended to trigger a map update. Without calling

      mapUpdater.updateCatalog(...)

  , the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage. Note that calling
      updateCatalog(...)

  will update the version, only when a map update is available in the catalog.
  </p>

  **Notes**

  - The `LayerConfiguration` is only available for the Navigate licenses that contains the offline maps feature. It has no effect on other license.

  - The `LayerConfiguration` cannot be set separately for a region, it will be applied globally for all regions that will be downloaded in the future.

  - It is not possible to specify a separate `LayerConfiguration` for the map cache and offline maps. The `LayerConfiguration` will be always applied to both.

  - If a `LayerConfiguration` is applied, then only the listed features will be enabled, all others will be disabled. For example, if you want to disable only one feature, then all other features need to be present, or they will be also disabled.

  The `LayerConfiguration` controls which content will be subject of

  - map download for features in

        enabledFeatures()

    ,

  - explicit prefetching using `sdk.prefetcher.RoutePrefetcher, sdk.prefetcher.PolygonPrefetcher` and implicit prefetching, such as when displaying a map view, for features in

        implicitlyPrefetchedFeatures()

    .

  <a href="sdk-for-ios-explore-structs-layerconfiguration" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LayerConfiguration : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19LocalizedRoadNumberV"></span>` `<span id="//apple_ref/swift/Struct/LocalizedRoadNumber" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk19LocalizedRoadNumberV" class="token"><code>LocalizedRoadNumber</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Used to represent road number localized to specific language with optional direction and route type information.

  <a href="sdk-for-ios-explore-structs-localizedroadnumber" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocalizedRoadNumber : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20LocalizedRoadNumbersV"></span>` `<span id="//apple_ref/swift/Struct/LocalizedRoadNumbers" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk20LocalizedRoadNumbersV" class="token"><code>LocalizedRoadNumbers</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of multiple names or titles for the same entity, possibly in different languages.

  <a href="sdk-for-ios-explore-structs-localizedroadnumbers" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocalizedRoadNumbers : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13LocalizedTextV"></span>` `<span id="//apple_ref/swift/Struct/LocalizedText" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk13LocalizedTextV" class="token"><code>LocalizedText</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Used to represent text localized to specific language.

  <a href="sdk-for-ios-explore-structs-localizedtext" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocalizedText : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14LocalizedTextsV"></span>` `<span id="//apple_ref/swift/Struct/LocalizedTexts" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14LocalizedTextsV" class="token"><code>LocalizedTexts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of multiple names or titles for the same entity, possibly in different languages.

  <a href="sdk-for-ios-explore-structs-localizedtexts" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocalizedTexts : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LocationV"></span>` `<span id="//apple_ref/swift/Struct/Location" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8LocationV" class="token"><code>Location</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a location in the world at a given time.

  <a href="sdk-for-ios-explore-structs-location" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Location : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16LocationDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/LocationDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk16LocationDelegateP" class="token"><code>LocationDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications about location updates.

  <a href="sdk-for-ios-explore-protocols-locationdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol LocationDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14LocationSourceO"></span>` `<span id="//apple_ref/swift/Enum/LocationSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14LocationSourceO" class="token"><code>LocationSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates where the location was computed.

  Tells whether the location was calculated on the same device running HERE SDK or received from an external source.

  Example external sources: GNSS modules connected via serial (e.g., u-blox), or vehicle positioning systems.

  Example internal sources: positions computed on the same phone or embedded device using integrated GNSS or sensor fusion components.

  <a href="sdk-for-ios-explore-enums-locationsource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LocationSource : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18LocationTechnologyO"></span>` `<span id="//apple_ref/swift/Enum/LocationTechnology" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18LocationTechnologyO" class="token"><code>LocationTechnology</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Technology or provider of the location.

  <a href="sdk-for-ios-explore-enums-locationtechnology" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LocationTechnology : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12LocationTimeV"></span>` `<span id="//apple_ref/swift/Struct/LocationTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk12LocationTimeV" class="token"><code>LocationTime</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This struct presents all the time data tied to a location, like an arrival or departure time. The time data is originally specified in RFC 3339, section 5.6 format. For example, “2022-03-23T16:07:31+01:00” in Cracow, Poland, i.e. a Central European Time (CET) location. Note that this struct doesn’t give any data on the tied location. The location should be derived from the context.

  <a href="sdk-for-ios-explore-structs-locationtime" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocationTime : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11LogAppenderP"></span>` `<span id="//apple_ref/swift/Protocol/LogAppender" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11LogAppenderP" class="token"><code>LogAppender</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An interface to implement a listener to receive log messages.

  <a href="sdk-for-ios-explore-protocols-logappender" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol LogAppender : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LogControlC"></span>` `<span id="//apple_ref/swift/Class/LogControl" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10LogControlC" class="token"><code>LogControl</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class provides functionality to enable/disable console logs as well as setting a custom log appender to receive log messages from the SDK.

  <a href="sdk-for-ios-explore-classes-logcontrol" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LogControl
  ```

  ``` highlight
  extension LogControl: NativeBase
  ```

  ``` highlight
  extension LogControl: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LogLevelO"></span>` `<span id="//apple_ref/swift/Enum/LogLevel" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8LogLevelO" class="token"><code>LogLevel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Severity levels for log messages.

  <a href="sdk-for-ios-explore-enums-loglevel" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LogLevel : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8MetadataC"></span>` `<span id="//apple_ref/swift/Class/Metadata" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8MetadataC" class="token"><code>Metadata</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Holds metadata on behalf of a map item. An instance of this class can contain metadata items of varying types, such as String, Integer, Double, GeoCoordinates etc. and can also hold arbitrary metadata types by the use of the CustomMetadataValue protocol.

  <a href="sdk-for-ios-explore-classes-metadata" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Metadata
  ```

  ``` highlight
  extension Metadata: NativeBase
  ```

  ``` highlight
  extension Metadata: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12MetadataTypeO"></span>` `<span id="//apple_ref/swift/Enum/MetadataType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk12MetadataTypeO" class="token"><code>MetadataType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Different types of objects that can be stored in a Metadata class instance.

  <a href="sdk-for-ios-explore-enums-metadatatype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MetadataType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk6NameIDV"></span>` `<span id="//apple_ref/swift/Struct/NameID" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk6NameIDV" class="token"><code>NameID</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Structure to represent name-id pairs.

  <a href="sdk-for-ios-explore-structs-nameid" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct NameID : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15NetworkEndpointV"></span>` `<span id="//apple_ref/swift/Struct/NetworkEndpoint" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk15NetworkEndpointV" class="token"><code>NetworkEndpoint</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Network endpoint.

  <a href="sdk-for-ios-explore-structs-networkendpoint" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct NetworkEndpoint : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15NetworkSettingsV"></span>` `<span id="//apple_ref/swift/Struct/NetworkSettings" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk15NetworkSettingsV" class="token"><code>NetworkSettings</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Network configuration to be used by <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a> during the initialization.

  <a href="sdk-for-ios-explore-structs-networksettings" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct NetworkSettings : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22ParameterConfigurationV"></span>` `<span id="//apple_ref/swift/Struct/ParameterConfiguration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk22ParameterConfigurationV" class="token"><code>ParameterConfiguration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains values of configurable parameters that are used in SDK. This is a BETA feature and thus there can be bugs and unexpected behavior.

  <a href="sdk-for-ios-explore-structs-parameterconfiguration" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ParameterConfiguration : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18PassThroughFeatureO"></span>` `<span id="//apple_ref/swift/Enum/PassThroughFeature" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18PassThroughFeatureO" class="token"><code>PassThroughFeature</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents features that are allowed to consume online data when the HERE SDK’s offline mode is activated via <a href="sdk-for-ios-explore-classes-sdknativeengine#/s:7heresdk15SDKNativeEngineC13isOfflineModeSbvp">`SDKNativeEngine.isOfflineMode`</a> and/or <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV11offlineModeSbvp">`SDKOptions.offlineMode`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-passthroughfeature" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PassThroughFeature : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9PowerTypeO"></span>` `<span id="//apple_ref/swift/Enum/PowerType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9PowerTypeO" class="token"><code>PowerType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the type of electrical power. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-powertype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PowerType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17PedestrianProfileV"></span>` `<span id="//apple_ref/swift/Struct/PedestrianProfile" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk17PedestrianProfileV" class="token"><code>PedestrianProfile</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains values of pedestrian profile. This is a BETA feature and thus there can be bugs and unexpected behavior.

  <a href="sdk-for-ios-explore-structs-pedestrianprofile" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `sdk.transport.TransportSpecification` instead.") public struct PedestrianProfile : Hashable
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11PickedPlaceV"></span>` `<span id="//apple_ref/swift/Struct/PickedPlace" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11PickedPlaceV" class="token"><code>PickedPlace</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Carries the result of picking a Carto POI (point of interest) object.

  <a href="sdk-for-ios-explore-structs-pickedplace" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PickedPlace : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17PlatformThreadingP"></span>` `<span id="//apple_ref/swift/Protocol/PlatformThreading" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk17PlatformThreadingP" class="token"><code>PlatformThreading</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for task activities on the main thread.

  <a href="sdk-for-ios-explore-protocols-platformthreading" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol PlatformThreading : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7Point2DV"></span>` `<span id="//apple_ref/swift/Struct/Point2D" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk7Point2DV" class="token"><code>Point2D</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a point in 2D space. When this point is used to indicate coordinates on a view, then (0,0) will mark the top-left corner of the view.

  <a href="sdk-for-ios-explore-structs-point2d" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Point2D : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7Point3DV"></span>` `<span id="//apple_ref/swift/Struct/Point3D" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk7Point3DV" class="token"><code>Point3D</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a point in 3D space.

  <a href="sdk-for-ios-explore-structs-point3d" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Point3D : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk39PolylineSimplificationCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/PolylineSimplificationCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk39PolylineSimplificationCompletionHandlera" class="token"><code>PolylineSimplificationCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method will be called on the main thread when

      PolylineSimplifier.simplify(...)

  is finished.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias PolylineSimplificationCompletionHandler = ( _ queryError : PolylineSimplificationError ?, _ result : [ GeoCoordinates ]?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>queryError</code></em><code> </code></td>
  <td><div>
  <p>The optional error, which occurred during simplification.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>result</code></em><code> </code></td>
  <td><div>
  <p>The simplified polyline with number of points less or equal to the input polyline of</p>
  <pre><code>PolylineSimplifier.simplify(...)</code></pre>
  .
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27PolylineSimplificationErrorO"></span>` `<span id="//apple_ref/swift/Enum/PolylineSimplificationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk27PolylineSimplificationErrorO" class="token"><code>PolylineSimplificationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error code which specifies, what went wrong during

      PolylineSimplifier.simplify(...)

  operation.
  </p>

  <a href="sdk-for-ios-explore-enums-polylinesimplificationerror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PolylineSimplificationError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18PolylineSimplifierC"></span>` `<span id="//apple_ref/swift/Class/PolylineSimplifier" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18PolylineSimplifierC" class="token"><code>PolylineSimplifier</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  PolylineSimplifier helps to reduce the number of points in the polyline by removing redundant elements using Douglas–Peucker algorithm, so that result stays within <a href="sdk-for-ios-explore-classes-polylinesimplifier-options">`PolylineSimplifier.Options`</a>.

  Typical use case is to perform input preparation step before invoking computationally heavy API. Such API have an upper limit on the input collection size and is subject to reduced performance when collection is huge. Examples of such API are:

  - <a href="sdk-for-ios-explore-classes-trafficengine">`TrafficEngine`</a> methods which accept a <a href="sdk-for-ios-explore-structs-geocorridor">`GeoCorridor`</a>;
  - `RoutePrefetcher.prefetchGeoCorridor`.

  <a href="sdk-for-ios-explore-classes-polylinesimplifier" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PolylineSimplifier
  ```

  ``` highlight
  extension PolylineSimplifier: NativeBase
  ```

  ``` highlight
  extension PolylineSimplifier: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13ProxySettingsV"></span>` `<span id="//apple_ref/swift/Struct/ProxySettings" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk13ProxySettingsV" class="token"><code>ProxySettings</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Proxy configuration for the HERE SDK network that is applied per request. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-proxysettings" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ProxySettings : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11Rectangle2DV"></span>` `<span id="//apple_ref/swift/Struct/Rectangle2D" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11Rectangle2DV" class="token"><code>Rectangle2D</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a 2D rectangle defined by the origin and size.

  <a href="sdk-for-ios-explore-structs-rectangle2d" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Rectangle2D : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9RouteTypeO"></span>` `<span id="//apple_ref/swift/Enum/RouteType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9RouteTypeO" class="token"><code>RouteType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the level of significance of a route in a range from 1 to 6. A value of 1 stands for the most major route and 6 the most minor. The route type indicates that the road’s name is actually a route number and in many countries is displayed in a shield symbol (e.g., Interstate and State routes in the U.S.). See <https://developer.here.com/documentation/here-map-content-schema/dev_guide/topics_schema/streetname.routetype.html>

  <a href="sdk-for-ios-explore-enums-routetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RouteType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8RunnableP"></span>` `<span id="//apple_ref/swift/Protocol/Runnable" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8RunnableP" class="token"><code>Runnable</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol that should be implemented by any class whose instances are intended to be executed by a thread.

  <a href="sdk-for-ios-explore-protocols-runnable" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol Runnable : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19SDKBuildInformationC"></span>` `<span id="//apple_ref/swift/Class/SDKBuildInformation" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk19SDKBuildInformationC" class="token"><code>SDKBuildInformation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The SDKBuildInformation class is designed to provide information about the SDK build.

  <a href="sdk-for-ios-explore-classes-sdkbuildinformation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKBuildInformation
  ```

  ``` highlight
  extension SDKBuildInformation: NativeBase
  ```

  ``` highlight
  extension SDKBuildInformation: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8SDKCacheC"></span>` `<span id="//apple_ref/swift/Class/SDKCache" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8SDKCacheC" class="token"><code>SDKCache</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class to manage SDK Cache. Path for SDKCache is specified via <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV9cachePathSSvp">`SDKOptions.cachePath`</a>. SDKCache manages temporary downloaded map data during map interaction and follows LRU (least recently used) strategy to delete map data when cache size exceeds the specified <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV16cacheSizeInBytess5Int64Vvp">`SDKOptions.cacheSizeInBytes`</a>.

  <a href="sdk-for-ios-explore-classes-sdkcache" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKCache
  ```

  ``` highlight
  extension SDKCache: NativeBase
  ```

  ``` highlight
  extension SDKCache: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/c:@M@heresdk@objc(cs)SDKInternalInitializer"></span>` `<span id="//apple_ref/swift/Class/SDKInternalInitializer" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/c:@M@heresdk@objc(cs)SDKInternalInitializer" class="token"><code>SDKInternalInitializer</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class is used to initialize internals of the SDK. Usually shouldn’t be used directly.

  <a href="sdk-for-ios-explore-classes-sdkinternalinitializer" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKInternalInitializer : NSObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9SDKLoggerC"></span>` `<span id="//apple_ref/swift/Class/SDKLogger" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9SDKLoggerC" class="token"><code>SDKLogger</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Logging interface for Android/iOS platforms. These logs are under management of <a href="sdk-for-ios-explore-classes-logcontrol">`LogControl`</a> and should be used instead of platform-specific logging functions.

  <a href="sdk-for-ios-explore-classes-sdklogger" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKLogger
  ```

  ``` highlight
  extension SDKLogger: NativeBase
  ```

  ``` highlight
  extension SDKLogger: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15SDKNativeEngineC"></span>` `<span id="//apple_ref/swift/Class/SDKNativeEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk15SDKNativeEngineC" class="token"><code>SDKNativeEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Holds internal services and configurations needed by various HERE SDK modules.

  You can initialize the HERE SDK in two ways:

  - Create a shared instance of the `SDKNativeEngine` with

        SDKNativeEngine.makeSharedInstance()

    .

  - Create individual instances of the `SDKNativeEngine` via

        SDKNativeEngine()

    . Note that this does not automatically set a shared instance.

  <a href="sdk-for-ios-explore-classes-sdknativeengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKNativeEngine
  ```

  ``` highlight
  extension SDKNativeEngine: NativeBase
  ```

  ``` highlight
  extension SDKNativeEngine: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/c:@M@heresdk@objc(cs)SDKNativeEngineHolder"></span>` `<span id="//apple_ref/swift/Class/SDKNativeEngineHolder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/c:@M@heresdk@objc(cs)SDKNativeEngineHolder" class="token"><code>SDKNativeEngineHolder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKNativeEngineHolder : NSObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV"></span>` `<span id="//apple_ref/swift/Struct/SDKOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10SDKOptionsV" class="token"><code>SDKOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  SDKOptions provide an alternative way to set or update the HERE SDK credentials and other parameters at runtime to initialize the <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a>.

  <a href="sdk-for-ios-explore-structs-sdkoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SDKOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKVersionV"></span>` `<span id="//apple_ref/swift/Struct/SDKVersion" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10SDKVersionV" class="token"><code>SDKVersion</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The `SDKVersion` represents version information for an SDK product. It encapsulates various attributes related to the version, including product variant, version details and backend configuration. Please note, `sdk.core.engine.SDKBuildInformation` can be used to get `SDKVersion`.

  <a href="sdk-for-ios-explore-structs-sdkversion" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SDKVersion : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk6Size2DV"></span>` `<span id="//apple_ref/swift/Struct/Size2D" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk6Size2DV" class="token"><code>Size2D</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the size of a 2D structure.

  <a href="sdk-for-ios-explore-structs-size2d" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Size2D : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:SS"></span>` `<span id="//apple_ref/swift/Extension/String" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:SS" class="token"><code>String</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  extension String : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21TaskCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/TaskCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk21TaskCompletionHandlera" class="token"><code>TaskCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method will be called on the main thread when a task call has been completed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias TaskCompletionHandler = ( _ taskOutcome : TaskOutcome ) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>taskOutcome</code></em><code> </code></td>
  <td><div>
  <p>The task outcome</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10TaskHandleP"></span>` `<span id="//apple_ref/swift/Protocol/TaskHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10TaskHandleP" class="token"><code>TaskHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Handle used for the manipulation of the task.

  <a href="sdk-for-ios-explore-protocols-taskhandle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TaskHandle : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11TaskOutcomeO"></span>` `<span id="//apple_ref/swift/Enum/TaskOutcome" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11TaskOutcomeO" class="token"><code>TaskOutcome</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum represents that a task has been completed. Refer to <a href="sdk-for-ios-explore-core#/s:7heresdk21TaskCompletionHandlera">`TaskCompletionHandler`</a> for more details.

  <a href="sdk-for-ios-explore-enums-taskoutcome" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TaskOutcome : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9ThreadingC"></span>` `<span id="//apple_ref/swift/Class/Threading" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9ThreadingC" class="token"><code>Threading</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initializes threading support on native side.

  <a href="sdk-for-ios-explore-classes-threading" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Threading
  ```

  ``` highlight
  extension Threading: NativeBase
  ```

  ``` highlight
  extension Threading: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8TimeRuleC"></span>` `<span id="//apple_ref/swift/Class/TimeRule" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8TimeRuleC" class="token"><code>TimeRule</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification. For example: -\*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents: March 2nd Sunday 02h:00m for 9 months ONLY DURING November 1st Sunday 02h:00m from 9 months ago BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00

  The operator \* represents reccuring occurrence, `+` represents a logical OR operation and `-` represents exclusion meaning, BUT NOT operations.

  This example string represents a time period that meets the following criteria:

  - `M3f21h2`: M3 denotes third month of the year, i.e. March, f2 stands for the second Sunday of the month (as “f” might indicate “first”, “second”, “third”, etc.), 1 stands for the day of the week (1…7, Day of week, Sunday = day 1), and h2 represents the hour of the day (02:00) in 24 hour format.

  - `{M9}`: This denotes “for 9 months”, with “M9” standing for nine months. The brackets {} indicate a duration.

  - `M11f12h2`: M11 denotes 11th month of the year, i.e. November, f1 stands for the first Monday of the month, 2 stands for the day of the week (1…7, Day of week, Monday = day 2), and h2 represents the hour of the day (02:00) in 24 hour format.

  - {-M9}: This denotes “9 months ago from the current stated time”, with “-M9” standing for nine months in the past.

  -     (h15){h2}(h20){h2}

    : 15:00 to 17:00 OR 20:00 to 22:00 The brackets {} denotes duration, and the negative sign - represents a past duration.

  Note: The time period is a logical AND (&&) combination of two components or points in time and it only applies if a point in time is in both components.

  For more advanced examples of `TimeRule` see <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html#time-domain-advanced-examples">here</a>.

  <a href="sdk-for-ios-explore-classes-timerule" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TimeRule
  ```

  ``` highlight
  extension TimeRule: NativeBase
  ```

  ``` highlight
  extension TimeRule: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TransportProfileV"></span>` `<span id="//apple_ref/swift/Struct/TransportProfile" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk16TransportProfileV" class="token"><code>TransportProfile</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains values of transport profile. This is a BETA feature and thus there can be bugs and unexpected behavior.

  <a href="sdk-for-ios-explore-structs-transportprofile" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `TransportSpecification` instead.") public struct TransportProfile : Hashable
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/c:objc(cs)UIColor"></span>` `<span id="//apple_ref/swift/Extension/UIColor" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/c:objc(cs)UIColor" class="token"><code>UIColor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-explore-extensions-uicolor" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  extension UIColor
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UnitSystemO"></span>` `<span id="//apple_ref/swift/Enum/UnitSystem" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10UnitSystemO" class="token"><code>UnitSystem</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the available unit systems(imperial/metric).

  <a href="sdk-for-ios-explore-enums-unitsystem" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum UnitSystem : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV"></span>` `<span id="//apple_ref/swift/Struct/UsageStats" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10UsageStatsV" class="token"><code>UsageStats</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-usagestats" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct UsageStats
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 <a href="sdk-for-ios-explore" class="link" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

</div>


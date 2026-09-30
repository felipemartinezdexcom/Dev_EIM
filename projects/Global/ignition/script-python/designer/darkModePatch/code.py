'''
Standard Java Imports:
'''
from java.awt import AWTEvent, Color, Dimension, Toolkit, Window
from java.awt.event import ActionListener, AWTEventListener, ContainerListener, ItemListener, MouseAdapter
from java.awt.image import BufferedImage
from java.beans import PropertyChangeListener
from javax.swing import JCheckBoxMenuItem, JSplitPane, JViewport, SwingUtilities
from javax.swing.event import AncestorListener, DocumentListener, TableColumnModelListener, TreeModelListener
from javax.swing.table import DefaultTableCellRenderer
from javax.swing.text import SimpleAttributeSet, StyleConstants
from javax.swing.tree import DefaultTreeCellRenderer

'''
Ignition Specific Imports:
'''
# Validate all Ignition packages before importing,
# ...so the script won't fail if the packatge configuration ever changes
# ...such as could be the case with the upcomming 8.3 upgrade
def isPackageInstalled(basePackage, subPackage):
	return hasattr(__import__(basePackage, fromlist=[subPackage]), subPackage)

# This ignition import is critial to the main point of focus for the dark theme: the script editors
namedThemeExists = isPackageInstalled('com.inductiveautomation.ignition.common.gui', 'NamedTheme')
if namedThemeExists:
	from com.inductiveautomation.ignition.common.gui import NamedTheme

# This import sed in the Perspective property inspector in conjunction with SwingUtilities.getAncestorOfClass
# Recursive class name searches are inefficient here because there are multiple node editor class names.
# Consequently, the traditional approach is used even though it creates an ignition import dependancy,
# ...and a package validation is used to ensure there's no chance of throwing an exception
# ...if this package ever structure changes
isJsonEditInstalled = isPackageInstalled('com.inductiveautomation.ignition.client', 'jsonedit')
if isJsonEditInstalled:
	from com.inductiveautomation.ignition.client.jsonedit import NodeEditor

# This is known to used in Vision and to play nice with the look and feel,
# ...and it is probable that it's used in all designer installs the same way,
# ...but this is subject to change, and therefore should be validated to safeguard against future updates or configuration changes
isPlafInstalled = isPackageInstalled('com.inductiveautomation', 'plaf')
if isPlafInstalled:
	from com.inductiveautomation.plaf import ComboListCellRenderer

'''
Patch Parameters:
'''
# A list of components to paint with an almost black background and white forground
abwList = [# Generic Stuff:
	'JTableHeader', # Found over the import JDialog table
	'FPMIApp', 
	
	# Specialized Classes:
	'ActionCollectionEditor', # Perspective event editor right side outer pane
	'BindingEditor$PreviewPanel', # Lives at the bottom of the Perspective binding editor (Binding Preview)
	'ConfigHeader', # Perspective editor splash page upper level panel
	'CustomMethodEditor', # Perspective script editor-->custom method editor
	'DataPanelEditor', # Main body of the data tab of the reporting pane
	'DesignPanel$LayerParent', # Background of the pane behind the main design editor panes
	'DocumentShapeConfigFactory$DocumentShapeConfigPanel', # Propery inspector paper settings in the report module
	'GroupSearchProvider$SelectionPanel', # (ctrl - f) find/replace SQL Bridge group dropdown menu
	'GroupSearchProvider$SelectionPanel$SelectionRadio', # (ctrl - f) find/replace SQL Bridge group dropdown menu radio buttons
	'IndirectTagBindingConfigurator$RefTable', # Table in the indirect bindings area of the Vision binding editor
	'MessageHandlerEditor', # Perspective script editor-->message handler editor
	'NamedQueryPathSelector', # Search Icon located in the query tab of the Perspective binding editor
	'NamedQuerySearchProvider$SelectionPanel', # (ctrl - f) find/replace dropdown menu
	'NamedQuerySearchProvider$SelectionPanel$SelectionRadio',  # (ctrl - f) find/replace dropdown menu radio buttons
	'OverviewPanel', #Main splash area of the Report overview tab of the reporting module
	'OverviewPanel$NextScheduledRunLabel', # Right upper label in the Report overview tab of the reporting module
	'OverviewPanel$RunReportLabel', # Left upper label in the Report overview tab of the reporting module
	'PagesConfigPanel', # Perspective editor splash page mid level panel
	'ParameterEditorPanel', # background for the panel behind the expression editor found in the data tab of the reporting pane
	'RecentlyModified', # Perspective editor splash page lower level panel
	'SortableTable', # Located in query browser, find/replace window, and possibly other places in the designer
	'SyntheticaSafeGroupList', # Left side of the Vision binding popup. It is the selection list
	'TagBindingDesignDelegate$ConfigPanel$DirectTagConfigPanel', # Lives in the Tag area of the Perspective binding popup
	'TagSearchProvider$SelectionUI',  # (ctrl - f) find/replace tag provider dropdown menu
	'TagSearchProvider$SelectionUI$ProviderCheckBox', # (ctrl - f) find/replace tag provider dropdown menu checkboxes
	'ViewSearchProvider$SelectionPanel', # (ctrl - f) find/replace view selection dropdown menu
	'ViewSearchProvider$SelectionPanel$SelectionRadio', # (ctrl - f) find/replace view selection dropdown menu radio buttons	
	'VisionSearchProvider$SelectionPanel',  # (ctrl - f) find/replace window dropdown menu
	'VisionSearchProvider$SelectionPanel$SelectionRadio']  # (ctrl - f) find/replace window dropdown menu radio buttons

#	# A list of components to paint with a black background and white forground
bwList = [# Generic stuff:
	'HeaderLabel',
	'JDialog', # Import manager and probably other gui locking popups
	'JToolBar', # Known to be at the top of the Vision Property Editor, and perhaps other places in the designer
	'JideTable', # Known to be in the schedule tab of the reporting module
	'JTable',
	'JideToolbarButton',
	'JideToggleButton',
	'JLayeredPane', # Usually filled with stuff, but are visible in some inactive floating dialogs 
	'JSVGCanvas', # This is the canvas that renders the selected SVG in the symbol factory
	'JTextPane',
	
	# Specialized classes:

	'AboutDialog$1', # [Help-->About] Ignition popup
	'ActionConfigPanel$DocumentationPanel$2',# Found at the bottom of the Vision component script editor
	'ActionConfigPanel$DocumentationPanel$3', # Found at the bottom of the Vision component script editor
	'Box', # Located behind the buttons in the import JDialog popup
	'BorderChooser', # Vision popup for selecting borders
	'Box$Filler', # This is the area underneath the collapible panes when the Vision component pallet has been filtered or collapsed
	'ComponentScopeEditor$BindingCompatibleNodeEditor$BindingControl', # Perspective binding icons
	'CollapsiblePanePalette$2',# Sits above the component Pallet. Has a search icon that's a dropdown, and the nav filter has a textfield
	'CollapsiblePanePalette$GroupView$View', # These are collapsable lists in the component pallet area
	'CommandBar$a', # This is a class of button that is found in certain tool bars such as the Vision shape editing toolbar
	'ComponentPaletteFilterField', # This is the search field above the component pallet in the Perspective module
	'ContentContainer', # The background container for 'JideSplitButton' This changes the color without removing the button's highlight behavior
	'CustomFunctionEditor', # Custom function area of the component script editor for Vision
	'DefaultToolBar', # Used in image management panel
	'ErrorStrip', # This is the strip on the right side of the script console that shows where search results and errors are
	'ExpressionStructureBindingDesignDelegate$ConfigPanel$1$1', # Expression Structure configuration pane in the Perspective binding editor
	'FilterablePalette$2', # This is a JList that's added to Perspective component pallet when filtering components
	'FindReplaceToolbar', # Script console search bar
	'FormatTransformDesignDelegate$ConfigPanel', # Outer format transform panel of the Perspective binding editor
	'FormatTransformDesignDelegate$ConfigPanel$NumericModePanel', # Inner format transform panel of the Perspective binding editor
	'FrameContainer', # Found in dockable containers such as the reporting module's propery inspector
	'Gutter', # This is the container for line numbers on the left side of the script console
	'Header1', # Labels in main splash page of Perspective editor
	'HierarchialTranslationTable', # Contains the buttons on the right hand side of the translation manager
	'HolderPanel', # Found in the new transforms popup panel of the Perspective binding editor
	'IconButton', # Buttons in the vertical tool bar if the Vision Component Script Editor and possibly other places in the designer
	'LayoutConstraintsPanel',  # Revealed by right clicking and selecting "Layout" from a Vision component
	'LineNumberList', # These are the line numbers themselves in the script console
	'LocalizedLabel', # Locale dependant labels that are dispersed throughout the designer
	'MapTransformDesignDelegate$ConfigPanel', # Map transform panel of the Perspective binding editor
	'MapTransformDesignDelegate$ConfigPanel$MappingTable', # Map transform table of the Perspective binding editor
	'MenuEditor', # Vision client events menu editor panel
	'MenuEditor$MenuNodeEditor', # Found in the Vision client events editor, a subclass of the menu editor, and in painting, a small horizontal line on the right side of the editor
	'NavTreePanel$NavTreeFilterField', # Sits above the project browser. Has a search icon that's a dropdown, and the nav filter has a textfield
	'NodeEditor', # The JSON Editor's root panel
	'ParameterTable', # Named Query authoring area
	'PlaceholderPanel', # Found in the no binding area of the Perspective binding editor
	'PropertyEditorFrame$1', # Sits above the Perspective property editor. Has a search icon that's a dropdown, and the nav filter has a textfield
	'PropertyPane$a', # Buttons in the Vision Property Editor
	'RecentlyModified$RecentViewsTiles$Tile', # Selectable view tiles at the bottom of the main splash page of Perspective editor
	'ReportingPalette$CategoryView$ShapePaletteItem', # This is the component selector in the reporting module
	'ResizableDialog$1', # Outermost colorable object in floating dockable designer windows AND Border around dockable windows
	'RowNumberMargin', # Row number column of the expression editor in the data tab of the reporting module
	'ScriptTab', # A strip that sits above the library script editor that contains the label showing the current script edited and a the scope hint dropdown
	'SecurityTable',  # Named Query settings area
	'SimpleTreeTable$TreeHeader', # Tag browser table header
	'TabbedPanePalette', # Vision component pallet tabbed
	'TagToolbar', # Upper button bar in the tag browser
	'TemplateCanvasCustomizer$ParamsPanel', # When a template is selected, this is behind the custom properties list in the teplate canvas customizer popup
	'ThumbnailGallery', # Symbol Factory thumnail Pane
	'TranslationManager$LanguagePanel', # Language list on the left hand side of the translation manager
	'VerticalToolbar'] # Located to the right of the Vision Component Script Editor and possibly other places in the designer

specialContainerList = ['SlidingOverFrameContainer', # This container adds a hidden pane when the mouse cusror enters the tab on side of the designer, or when the tab is clicked and the pane is hidden
	'JSplitPane']

# A list of components to make opaque during dark mode
darkModeOpacityList = [ # Generic Stuff:
	'IconButton',
	'JideToolbarButton',
	'JideToggleButton',
	'JPanel',
	'JLayeredPane', # Usually filled with stuff, but are visible in some inactive floating dialogs 
	'JToolBar', # Known to be at the top of the Vision Property Editor, and perhaps other places in the designer
	'ScrollablePanel', # Known to affect the appearance of the reporting module's property inspector
	'VerticalToolbar',

	# Specialized Classes:
	'ActionQualPanel', # Component script editor-->Set Tag Value tab-->Panel at the bottom of the editor
	
	# {[Vision border chooser popup sub panels]
	'BorderChooser$BevelBorderOption', 
	'BorderChooser$ButtonBorderOption',
	'BorderChooser$EtchedBorderOption',
	'BorderChooser$EtchedTitledBorderOption',
	'BorderChooser$FieldBorderOption',
	'BorderChooser$LineBorderOption',
	'BorderChooser$LineTitledBorderOption',
	'BorderChooser$MatteBorderOption',
	'BorderChooser$PanelTitledBorderOption',
	# [/Vision border chooser popup sub panels]}
	
	'CommandBar$a', # These are buttons on multiple command bars in the designer
	'ComponentBorderedPanel',
	'ComponentScopeEditor$BindingCompatibleNodeEditor$BindingControl', # Perspective binding icons
	'NamedQueryPathSelector', # Search Icon located in the query tab of the Perspective binding editor
	'PieChartConfigFactory$PieChartConfigPanel', # Reporting module pie chart property inspector
	'PropertyPane$a', # Buttons in the Vision Property Editor
	'ReportingPalette$CategoryView$ShapePaletteItem', # This is the component selector in the reporting module
	'RMDocumentTool$PageSizeView',
	'ScheduledParametersPanel', # In full screen, this normally transparent becomes visible as a white emtpy void at the bottom of the parameters tab of the schedule pane of the reporting module
	'ScriptEditorBuilder']

# A list of components to make transparent during dark mode
darkModeTransparencyList = ['DesignPanel$DesignableContainerLayer']

# A list of components to paint with a dark grey background and white forground
dgwList = [ # Generic Stuff:
	'ActionQualPanel',
	'ComponentBorderedPanel',
	'DockableBarContainer',
	'JTabbedPane',
	'JToggleButton',
	'JPanel',
	'JScrollBar',
	'JScrollPane$ScrollBar',
	'RecentlyModifiedTilePanel',
	'ResourceBuilderPanel',
	'ScriptEditorBuilder',
	'ScrollablePanel',
	'VerticalToolbar',
	
	# Specialized Classes:
	'AbstractSlidingConfigPanel$TitlePanel', # Found in the reporting module property inspecor's script editor. It contains the label above the editor
	'ActionConfigPanel$DocumentationPanel', # Found at the bottom of the Vision component script editor
	'ActionEditPanel', # Perspective event editor right half with script editor
	'AlarmJournalQueryConfigPanel', # A panel that is added to the data tab of the reporting module if a "Query - alarm journal data source is added and selected
	'AutoHideContainer', # Sideways and overhead tabs for slideover docking windows
	'BannerPanel$3', # Vision binding popup no binding banner
	'BindingEditor$TransformsPanel$TransformWrapperPanel', # Small strip under the main title pane of the script transform panel of the Perspective binding editor
	
	# {[Vision border chooser popup sub panels]:
	'BorderChooser$BevelBorderOption',
	'BorderChooser$ButtonBorderOption',
	'BorderChooser$EtchedBorderOption',
	'BorderChooser$EtchedTitledBorderOption',
	'BorderChooser$FieldBorderOption',
	'BorderChooser$LineBorderOption',
	'BorderChooser$LineTitledBorderOption',
	'BorderChooser$MatteBorderOption',
	'BorderChooser$PanelTitledBorderOption',
	# [/Vision border chooser popup sub panels]}
	
	'BottomButtonPanel', # Found at the bottom of the Perspective binding editor. It contains the OK, Cancel, and Apply buttons
	'ButtonPanel', # Found at the bottom of the tag editor. It contains the OK, Cancel, and Apply buttons
	'CalculationsPanel', # Appears under the JRadioButton Choice panel in the Tag History binding tab in the Perspective binding editor if the Calculations radio button is selected
	'ClientGeneralPropsPanel', # Found under [Project-->Properties-->Vision General]
	'ClientLaunchPropsPanel', # Found under [Project-->Properties-->Vision Launching]
	'ClientLoginPropsPanel', # Found under [Project-->Properties-->Vision Login]
	'ClientPollingPropsPanel', # Found under [Project-->Properties-->Vision Timing]
	'ClientUIPropsPanel', # Found under [Project-->Properties-->Vision User Interface]
	'ConfigurationExplorer$createBottomButtonPanel$1', # Perspective component configuration explorer, lower button panel
	'ConfigurationView', # Perspective component configuration explorer
	'DesignerGeneralPropsPanel', # Found under [Project-->Properties-->Project Designer]
	'DesignerWindowEditPropsPanel', # Found under [Project-->Properties-->Vision Design]
	'ExpandCollapsePanel', # Collapsable target options in the find/replace window
	'ExtensionFunctionEditor', # In the extension function editors of the Vision component script editor popup
	'ExtensionFunctionPanel', # Small strip seperating collapible panes in the script transform panel of the Perspective binding editor
	'HttpBindingDesignDelegate$ConfigPanel', # Main panel of the HTTP binding tab in the Perspective binding editor
	'JideTable$ab', #This is the header for the schedule table in the reporting module
	'JRadioButtonChoice', # A JPanel that holds the radio buttons encountered in multiple locations of the Perspective binding editor
	'LearnMoreLabel', # Main splash page link
	'NamedQueryChoicePanel', # Vision binding popup, Named query panel
	'NamedQueryPathPanel', # Vision binding popup, Named query panel, around the SELECT Query and UPDATE Query text boxes
	'PermissionsConfigurator', # Found under [Project-->Properties-->Perspective Permissions]
	'PerspectiveIdleTimeoutPropsPanel', # Found under [Project-->Properties-->Perspective Inactivity]
	'PermissionsPropsPanel', # Found under [Project-->Properties-->Project Permissions]
	'PerspectivePropsPanel', # Found under [Project-->Properties-->Perspective General]
	'PieChartConfigFactory$PieChartConfigPanel', # Reporting module pie chart property inspector
	'PollingOptionPanel', # Panel the polling checkbox and textfield is located in in the Tag History binding area of the Perspective binding editor
	'ProjectExporter$1', # One of two outer panels of the [File-->Export] popup window
	'ProjectExporter$ExportPanel', # Two of two outer panels of the [File-->Export] popup window
	'ProjectGlobalPropsPanel', # Found under [Project-->Properties-->Project General]
	'QueryBindingDesignDelegate$ConfigPanel$1', # Panel behind auto the path and return format panes in the Perspective binding editor's query binding tab
	'QuickTableFilterField', # This is the underlay with a search icon dropdown button to the right of many textfields in the designer
	'RateOptionsPanel',  # Vision binding popup, Named query panel, area around teh Polling Mode options
	'RecentlyModifiedTablePanel', # Found on hte project library script page, and it contains a table with recently modified library scripts
	'SearchReplaceDialog$7', # This is the top level checkbox in the find / replace window (ctrl - f)
	'SearchReplaceDialog$TargetSettings$CategoryBox', # These are nested checkboxes in the find / replace window (ctrl - f)
	'ScriptTransformDesignDelegate$ScriptTransformEditor', # Main script transform panel in the Perspective binding editor
	'SimpleBoundTagConfigurator$TagBindingOptionsPanel',
	'SortableTableHeader', # Found in translation manager and find/replace window
	'StatusBar', # Perspective configuration explorer. This is actually a label over the details box
	'TagDropConfigPropsPanel', # Found under [Project-->Properties-->Perspective Tag Drop]
	'TagDropConfigPropsPanel$BindingsTablePanel', # Found under [Project-->Properties-->Perspective Tag Drop]
	'TagDropConfigPropsPanel$DataTypeTablePanel', # Found under [Project-->Properties-->Perspective Tag Drop]
	'TagHistoryBindingConfigPanel', # Main panel of the Tag History binding tab in the Perspective binding editor
	'TagHistoryBindingConfigPanel$QueryModePanel', # Contains dropdown for query mode and point count field in the Tag History binding tab in the Perspective binding editor
	'TagHistoryBindingConfigPanel$TimeRangePanel', # Contains the time range dropdown and most recent selection area in the Tag History binding tab in the Perspective binding editor
	'TagSelectionPanel', # Lower level binding pane in the Tag History binding tab in the Perspective binding editor
	'TagSelectionPanel$DirectSelectionPanel'] # Holds a table in the tag selection panel in the Tag History binding tab in the Perspective binding editor

# Used to skip iterations where  project stuff would otherwise get inadvertently colored
exclusionList = ['FilterablePalette', # Found in the Perspective component pallet when the filter textbox is being used. It has a write only attribute components that causes the script to fail.
	'InspectorFrame$CustomPropertyTable', # Going any further with the coloring of the property table looks spotty, and can be difficult to use
	'PropertyTablePanel$CustomPropertyTable' # Going any further with the coloring of the property table looks spotty, and can be difficult to use
	]

# Heavyweight popups are not 
heavyWeightPopupListenerList = ['BorderlessField',
	'ComponentScopeEditor$BindingCompatibleNodeEditor$2',
	'Graphics2dRenderWidget', # Perspective view editor
	'InteractionLayer', # Vision designer canvas layer, overlays window and template editors
	'JTree', # jtrees, such as the library script nav panel, often have heavyweight pops
	'NavTreePanel$1', # Project navigation
	'NodeEditor$MainEditor',
	'NodeEditor$MainEditor$1',
	'PerspectiveKeyEditor',
	'TagFrameTree'] # Tag browser


# A list of buttons that have seperate enabled/disabled icons. These need to be flipped during dark mode,
# ...so that more contrast is created when enabled to make the component look enabled on a dark background,
# ...and to make the icons have less contrast when disabled to make the component look disabled in dark mode
iconFlipList = [ # Generic Stuff:
	'JButton', # This is used above the diagnostic console, and perhaps elsewhere in the designer
	'JideButton',
	'JideSplitButton',
	'JideToggleButton',
	'JideToolbarButton',
	'JToggleButton', # This is used above the diagnostic console, and perhaps elsewhere in the designer
			
	# Specialized Classes:
	'CommandBar$a',  # These are buttons on multiple command bars in the designer
	'CreateTagButton',
	'DataSetEditorDialog$DatasetEditorPanel$4', # This is the add column button in the dataset editor
	'JToolBar$1', # These are every icon button except the add column button in the dataset editor
	'OptionsButton',
	'PropertyPane$a'] # Buttons in the Vision Property Editor

# A list of components to paint with a light grey background and black forground
lgbList = [ # Generic Stuff:
	'JButton',
	'JComboBox',
	'JList',
	'JMenu',
	'JMenuBar',
	'JideTabbedPane',
	'JViewport',
	'JYTextField',
	'WindowWorkspace',
							
	# Specialized Classes:
	'AbstractBrowsableGalleryPanel$SearchField',
	'BorderChooser$BorderOption$2',
	'CategoryDetailPanel', # Inner panel behind the all properties area of the tag browser
	'CategoryListPanel', # Panel behind the all properties area of the tag browser
	'CheckBoxTree', # This is the checkbox tree found in the [File-->Export] popup
	'CodeEditorPainter', # Located in query browser
	'CodeEditor$DisplayTrackingSyntaxTextArea', # The script editor in the Named Query module
	'DBBrowserConfigurator', # Vision binding popup
	'DBBrowserPanel',
	'DBBrowserPanel$KeyPanel',
	'ExpressionConfigurator', # Vision binding popup
	'ExtensionFunctionPanel$ParametersPanel', # Dropdown pane in the Script transform panel of the Perspective binding editor
	'HierarchicalTable', # Found in translation manager
	'ImageBrowser$ThumbnailPanel', # Image library browser behind the thumnbnails
	'IndirectTagBindingConfigurator', # Vision binding popup
	'KeyboardEditor$LayoutList', # Background panel for right keyboard layout list in the [Tools --> Keyboard Layout] window
	'NamedQueryConfigurator', # Vision binding popup
	'PageAndDockEditor', # Perspective main splash page inner page configuration panel
	'Ruler$XAxis', # Vision X-Axis Ruler
	'Ruler$YAxis', # Vision Y-Axis Ruler
	'ScheduledParametersPanel', # In full screen, this normally transparent becomes visible as a white emtpy void at the bottom of the parameters tab of the schedule pane of the reporting module
	'ScheduledParametersPanel$ParameterDetailPanel', # Lower panel in the parameters tab of the schedule pane of the reporting module
	'SecurityLevelTree', # Found under [Project-->Properties-->Perspective Permissions]
	'SetToConstantConfigurator', # Vision binding popup
	'SimpleBoundColorConfigurator', # Found in some of the property binding popups in Vision
	'SimpleBoundTagConfigurator', # Vision binding popup
	'SimpleBoundPropertyConfigurator', # Vision binding popup
	'SlideOverPane', # Found in translation manager and undoubtably, numerous other places in the designer
	'SQLConfigurator', # Vision binding popup
	'StandardBannerPanel'] # Vision binding popup upper banner
	
# A list of components to paint with a light light grey background and white forground
llgbList = [ # Generic Stuff:
	'JTextArea',
	'JTextField',
	'JFormattedTextField', # Located in query browser and possibly other places in the designer
	
	# Specialized Classes:
	'JSpinner$NumberEditor',
	'OverlayTextField'] # Found in translation manager and perhaps other places in the designer

paintedPopups = [ # Generic Stuff:
	'JidePopupMenu',
	'JPopupMenu',
	
	# Specialized Classes:
	'ChoicePicker', # Perspecpective prop editor down arrows
	'ComponentPopup',
	'DataPanel$NewPopupMenu', # This popup is revealed by the plus arrow in the data tab of the report editor
	'JsonEditor$AddNodeMenu', # Revealed by pressing the plus Icon for Add Object Member in the Configure Expression area of the Perspective binding editor
	'NodeEditor$MainEditor$NodeContextMenu',
	'TagPopupMenu'] # Tag editor

# These are the names of the main stand alone windows
targetList = ['ActionEditorFrame', # Perspective component action script editor
	'BindingEditorFrame', # Perspective Binding Editor
	'BindingEditor$TransformsPanel$NewTransformPicker', # Perspective Binding Editor's "Add Transform" popup
	'ClientScriptEditor',
	'CollapsiblePanePalette',
	'ComponentScriptEditor',
	'ConfigurationExplorer', # Perspective component configuration explorerer
	'ComponentSecurityPanel', # Found in the security settings pane
	'CustomizerDialog', # Vision custom property and style customizer editors
	'DataSetEditorDialog', # Pops up when clicking on a dataset property's icon
	'DefaultPopupWindowParent',
	'DialogFloatingContainer',
	'DynamicOptsDialog', # Vision Binding Editor
	'FillAndStrokePane',
	'GlobalScriptEditor',
	'IgnitionDesigner',
	'InspectorFrame', # Reporting module property inspector
	'InteractiveScriptPlayground',
	'ImageManager',
	'JDialog', # Used for miscellaneous popups
	'KeyboardEditor',
	'KeysFrame', # Reporting module key browser
	'LayoutDialog', # Revealed by right clicking and selecting "Layout" from a Vision component
	'NamedStyleEditorFrame', # used in Perspectective to create a new sytle sheet
	'NavTreePanel',
	'NewViewDialog', # Perspective new view window. Revealed from nav the tree by right clicking a Perspective folder and selecting "New View" in the resultant popup
	'OPCBrowserPanel',
	'OutputConsoleParent',
	'PaletteFrame', # Perspective Component selection pallet
	'PopupFactory$MediumWeightPopup$MediumWeightComponent', # These are usualy just tool tips, but sometimes they are lightweight dialogs that fit within their parent window
	#'Popup$HeavyWeightWindow', # DON"T Target!!! Use the heavyWeightPopupListenerList intead! Used for various right click mouse click popup menus - Doesn't trigger dispatch event and slows down nav tree popup significantly
	'PositionDialog', # Revealed by right clicking and selecting "Size and Position" from a Vision component
	'ProjectExporter$2', # Displayed from [File-->Export]
	'PropertyEditorDialog',
	'PropertyEditorFrame', # Perspective property editor
	'PropertyTablePanel', # Vision component property pane
	'QueryBrowser',
	'ResizableWindow', # Perspective editor popups
	'ScriptEditorFrame', # Perspect custom method and message handler editor pane
	'SearchReplaceDialog', # Displayed by pressing ctrl + f  ### NEEDS WORK ###
	'SessionEventDialog', # Perspective session event script editor
	'SwingBorderEditor$BorderDialog', # Vision border editor that pops up when the pencil icon is pressed
	'SymbolBrowserFrame', # Popup window located @ [Tools --> Symbol Factory]
	'TabbedPanePalette',
	'TagBrowserFrame',
	'TagEditorDialog', # Revealed by double clicking a tag in the tag browser
	'TagObjectEditor', # Revealed by double clicking a Vision client tag in the tag browser
	'TranslationManager',
	'UdtPropBindingFrame'] # Revealed by clicking on certain parameter binding icons in the tag editor

# Assign reused colors to single, easy to use variables
black = system.gui.color('black')
white = system.gui.color('white')
almostBlack = system.gui.color(41, 49, 52)
darkGrey = system.gui.color(96, 96, 96)
defaultHighlightColor = system.gui.color(255, 255, 160) # Used for script highlighting, if the named themes import fails
defaultSelectionColor = system.gui.color(72, 169, 230) # This color is default in bright mode, but is used in dark mode because it contrasts well with both white and black text
menuItemBGColor = system.gui.color(int(darkGrey.red * 0.84), int(darkGrey.green * 0.93), darkGrey.blue)
lightGrey = system.gui.color(180, 180, 180)
lightlightGrey = system.gui.color(241, 241, 241)

if namedThemeExists:

	# Script editor DARK theme:
	darkScriptEditorTheme = NamedTheme.Dark.theme 								# Start with the predefined dark theme, and if desired, modify the following color properties:
	# darkScriptEditorTheme.activeLineRangeColor								# Unknown, did not observe any changes when manipulating this color during testing
	# darkScriptEditorTheme.armedFoldBG											# The fold indicators change to this color during mouseover
	# darkScriptEditorTheme.bgColor												# This is the main background color of the script editor
	# darkScriptEditorTheme.caretColor											# This is the color of the blinking text editor caret
	darkScriptEditorTheme.currentLineHighlight = system.gui.color(61, 61, 81)	# Highlights the entire selected line if there is only one line selected
	darkScriptEditorTheme.gutterBackgroundColor = black							# This a container that sits to the left of the script editor and contains all of the line numbers
	# darkScriptEditorTheme.gutterBorderColor 									# This is the line between the line number container and the text area
	# darkScriptEditorTheme.hyperlinkFG											# Unknown, did not observe any changes when manipulating this color during testing
	darkScriptEditorTheme.lineNumberColor = white								# This colors all of the line numbers to the left of the text editor				
	# darkScriptEditorTheme.marginLineColor										# Unknown, did not observe any changes when manipulating this color during testing
	# darkScriptEditorTheme.markAllHighlightColor								# This is the color of the non selected search results
	# darkScriptEditorTheme.markOccurrencesColor								# Unknown, did not observe any changes when manipulating this color during testing
	# darkScriptEditorTheme.matchedBracketBG									# Unknown, did not observe any changes when manipulating this color during testing
	# darkScriptEditorTheme.matchedBracketFG									# Unknown, did not observe any changes when manipulating this color during testing
	darkScriptEditorTheme.selectionBG = system.gui.color(192, 192, 192, 180)	# background color of the currently selected text
	# darkScriptEditorTheme.selectionFG											# Unknown, did not observe any changes when manipulating this color during testing
	
	# Script editor BRIGHT theme:
	# Nothing fancy here, just the standard theme
	lightScriptEditorTheme = NamedTheme.Default.theme

'''
Action Listeners
'''
# This is the control logic for the View checkbox that toggles between bright and dark modes
class DarkModeCheckBoxListener(ActionListener):
	def actionPerformed(self, event):
		applyPatch()
'''
Ancestor Listeners
'''
# This is used in the component script editor of Vision
# ...to detect when the script editor tab is selected apply the appropriate theme at that time.
# Otherwise, the tab theme will be lost every time the use selects it from a different tab.
class TabVisibilityListener(AncestorListener):
	def ancestorAdded(self, event):
		setPaintableComponents(event.source, None, True)
	
	def ancestorRemoved(self, event):
		pass
	
	def ancestorMoved(self, event):
		pass
		
'''
Container Listeners
'''
# Repaints containers in the designer when things are added to them
# Do NOT inadvertently use on the error strip in the script editors.
# ...When using the find textbox, the error strip will trigger a repaint for every item found
# ...because a line is added to the error strip for every item found.
class DarkModeContainerListener(ContainerListener):
	def componentAdded(self, event):
		# Initially paint anything that is visible at this event,, 
		# ...and schedule a followup painting attempt for after all other scheduled events,
		# ...so any internal changes that are to be made will end up getting painted,
		# ...with minimal choppiness appearant to the user.
		setPaintableComponents(event.source, event.source, getDarkMode())
		def delayPaint():
			setPaintableComponents(event.source, event.source, getDarkMode())
		if event.source.__class__.__name__ in ['DesignerToolbar', 'JPanel']:
			system.util.invokeLater(delayPaint)
	
	def componentRemoved(self, event):
		pass

'''
Document Listeners
'''
# Handles coloring the letters in any output console
class DarkModeDocumentListener(DocumentListener):
	
	# There are two known OEM listeners:
	# ...One is the expected text update listener,
	# ...and the other is for the caret
	
	# Wrapping the listeners together was the result of troubleshooting a buffer overflow bug
	# ...that was ultimately amiliorated but scheduling the color update using invoke later.
	# Therfore, it is possible that the order of operations is actualy unimportant,
	# ...and there is no actual need for wrapping the OEM listeners as long as the color update
	# ...is scheduled for after all currently scheduled actions in the EDT.
	# However, since a buffer overflow in the console breaks the designer and makes it completely unusable,
	# ...the order of oprations is strictly enforced with console document listener insert updates
	def __init__(self, originalListeners):
		self.originalListeners = originalListeners
	
	# Probably not applicable to the console which only ever adds or removes information
	def changedUpdate(self, event):
		for listener in self.originalListeners:
			listener.changedUpdate(event)

	# Do the normal updates first making sure they have been completed before updating the color
	def insertUpdate(self, event):
		for listener in self.originalListeners:
			listener.insertUpdate(event)
		
		# If this isn't scheduled at the end of the currently scheduled EDT thread actions,
		# ...it will can applied before the document is properly updated by the other listeners
		# ...resulting in a buffer overflow error
		def updateColor():
			
			# With the normal listener updates already scheduled in the EDT, define the new attributes [white forground text]
			# ...and apply them to the console document
			attributeSet = SimpleAttributeSet()
			StyleConstants.setForeground(attributeSet, white)  # Set the text color to white.
			event.document.setCharacterAttributes(event.offset, event.document.length, attributeSet, True)
		
		# Schedule the color update
		system.util.invokeLater(updateColor)		
	
	# Business as usual for clearing the console
	def removeUpdate(self, event):
		for listener in self.originalListeners:
			listener.removeUpdate(event)
'''
Mouse Listeners
'''
# Handles mouse action color effects in node editors throughout the designer
class DarkModeNodeHighlighter(MouseAdapter):
	def __init__(self, originalListener, nodeEditor):
		self.originalListener = originalListener
		self.nodeEditor = nodeEditor
		
		# The listener also has to exist on the JScrollPane due to the way the node editor is added by a JList
		self.viewport = SwingUtilities.getAncestorOfClass(JViewport, nodeEditor)
	
	def mouseEntered(self, event):
		self.refreshNodes(event)
		if self.nodeEditor: # Perspective's SESSION CUSTOM dropdown node lacks a node editor, so it's possible that others do as well
			self.mouseEnteredPainter(self.nodeEditor)

	def mouseExited(self, event):
		self.refreshNodes(event)
		if self.nodeEditor: # Perspective's SESSION CUSTOM dropdown node lacks a node editor, so it's possible that others do as well
			self.mouseExitedPainter(self.nodeEditor)
		
	def mouseEnteredPainter(self, nodeEditor):
		for component in nodeEditor.components:
			if component.__class__.__name__ == 'NodeEditor': # Stops subNodes from being highlighted
				return
			if component.__class__.__name__ == 'BorderlessField':
				component.background = darkGrey
			else:
				component.background = menuItemBGColor
			component.foreground = white
			self.mouseEnteredPainter(component)
		
	def mouseExitedPainter(self, nodeEditor):
		for component in nodeEditor.components:
			if component.__class__.__name__ == 'BorderlessField':
				component.background = almostBlack
			else:
				component.background = black
			component.foreground = white
			self.mouseExitedPainter(component)
	
	def refreshNodes(self, event):		
		# If the OEM highlight listener hadn't been added prior to the darkmode listener being added, 
		# ...find it and store it right away
		if self.originalListener is None:
			self.getOriginalListener(event.source)
			
		# Sweep all the other components for missing listeners and square them away
		# ...every time a node gets expanded, components get added that are missing the OEM hover listener.
		# ...To prevent flashes of white on mouse entry, all nodes are routinely swept to detect and correct this.
		if self.viewport: # Perspective's Session Custom dropdown lacks a viewport, so it's possible others do as well
			self.refreshNodeListeners(self.viewport)
		
	def getOriginalListener(self, component):
		for listener in component.mouseListeners:
			if listener.__class__.__name__ == 'HoverTracker$ComponentTracker':
				component.removeMouseListener(listener)
				component.addMouseListener(DarkModeNodeHighlighter(listener, getNodeEditor(component)))
				component.removeMouseListener(self)
				
	def refreshNodeListeners(self, viewport):
		for component in viewport.components:
			hoverListener = None
			darkModeListeners = []
			for listener in component.mouseListeners:
				if listener.__class__.__name__ == 'HoverTracker$ComponentTracker':
					hoverListener = listener
				elif listener.__class__.__name__ == 'DarkModeNodeHighlighter':
					darkModeListeners.append(listener)
			
			# Do nothing if the dark mode listener is already in play, but the hover listener is not,
			# ...In dark mode, this is what is wanted.
			
			# If both listeners are in play, remove the hover listeer and store it in the darkmode listener
			if hoverListener and darkModeListeners: 
				component.removeMouseListener(hoverListener)
				component.addMouseListener(DarkModeNodeHighlighter(hoverListener, getNodeEditor(component)))
				for darkModeListener in darkModeListeners:
					component.removeMouseListener(darkModeListener)
			
			# If only the hover listener is in play. remove it and add a dark mode listener. 
			# ...Then, store the hover listener in the dark mode listener
			elif hoverListener: 
				component.removeMouseListener(hoverListener)
				component.addMouseListener(DarkModeNodeHighlighter(hoverListener, getNodeEditor(component)))
			
			# If no listeners are in play, get the darkMode listener pre installed
			elif not darkModeListeners:# 
				component.addMouseListener(DarkModeNodeHighlighter(None, getNodeEditor(component)))
			self.refreshNodeListeners(component)

# Created for module splash pages
# Creates a mouse enter and exit highlight effect on the project creation tiles
# Also used on JideToggle button, although in that case, the restore selections logic is redundant
# ...since the JideToggleButton uses a dark mode  item listener for its selected property
class HighlightListener(MouseAdapter):
	def __init__(self, originalListener):
		self.originalListener = originalListener
	
	def mouseEntered(self, event):
		self.originalListener.mouseEntered(event)
		if event.source.__class__.__name__ == 'ResourceBuilderPanel$CreateResourceTile':
			if event.source.background.red > 230:
				event.source.background = menuItemBGColor
			else:
				event.source.background = black
				self.setForeground(event, menuItemBGColor)
		elif event.source.enabled:
			event.source.background = white
		
	def mouseExited(self, event):
		self.originalListener.mouseExited(event)
		if event.source.__class__.__name__ == 'ResourceBuilderPanel$CreateResourceTile':
			if event.source.background.red < 230:
				event.source.background = black
				self.setForeground(event, white)
			else:
				event.source.background = lightGrey
		elif hasattr(event.source, 'selected') and event.source.selected:
			event.source.background = darkGrey
			self.restoreSelections(event)
		else:
			event.source.background = black
			
	def mousePressed(self, event):
		self.originalListener.mousePressed(event)
	
	def mouseClicked(self, event):
		self.originalListener.mouseClicked(event)
		if event.source.__class__.__name__ == 'ResourceBuilderPanel$CreateResourceTile':
			event.source.background = black
			self.setForeground(event, menuItemBGColor)
			self.restoreSelections(event)
	
	def mouseReleased(self, event):
		self.originalListener.mouseReleased(event)
		
	def restoreSelections(self, event):
		self.originalListener.mouseReleased(event)
		for component in event.source.parent.components:
			if component.__class__.__name__ == 'ResourceBuilderPanel$CreateResourceTile':
				if component.background.red > 230:
					component.background = menuItemBGColor
				else:
					component.background = black
					self.setForeground(event, menuItemBGColor)
		
			elif hasattr(component, 'selected') and component.selected:
				component.background = darkGrey
			else:
				component.background = black
		event.source.foreground = white
		
	def setForeground(self, event, color):
		for component in event.source.components:
			if hasattr(component, 'text') and component.text:
				component.foreground = color

# The class IconButton has a built in listener that reverts its forground color on mouse entry
# In light mode this would create a highlight or focus effect, but it makes the icon hard to see in dark mode
# This listener bypasses that while in darkmode and provides the highlight effect through the background instead
class IconSaverListener(MouseAdapter):
	def __init__(self, originalListener):
		self.originalListener = originalListener
	
	def mouseEntered(self, event):
		event.source.background = menuItemBGColor
		
	def mouseExited(self, event):
		event.source.background = black
			
	def mousePressed(self, event):
		self.originalListener.mousePressed(event)
	
	def mouseClicked(self, event):
		self.originalListener.mouseClicked(event)
	
	def mouseReleased(self, event):
		self.originalListener.mouseReleased(event)

# Create a listner that reapplies the selected property of all JySubMenu items
# ...after the BasicMenuUI listener has done all of its required work
class NonDeselectingListener(MouseAdapter):
	def __init__(self, originalListener):
		self.originalListener = originalListener
	
	def mouseEntered(self, event):
		self.originalListener.mouseEntered(event)
		self.restoreSelections(event)
		event.source.background = lightGrey
		if event.source.enabled or event.source.__class__.__name__ == 'JLabel': 
			event.source.foreground = black
		else:						
			event.source.foreground = white
		
	def mouseExited(self, event):
		self.originalListener.mouseExited(event)
		if hasattr(event.source, 'popupMenu') and event.source.popupMenu and event.source.popupMenu.__class__.__name__ == 'JPopupMenu':
			event.source.background = darkGrey
		else:
			event.source.background = menuItemBGColor
		if event.source.enabled and event.source.__class__.__name__ != 'JLabel':
			event.source.foreground = white
		else:						
			event.source.foreground = black
		
	def mousePressed(self, event):
		self.originalListener.mousePressed(event)
	
	def mouseClicked(self, event):
		self.originalListener.mouseClicked(event)
	
	def mouseReleased(self, event):
		self.originalListener.mouseReleased(event)
		
	def restoreSelections(self, event):
		for component in event.source.parent.components:
			if hasattr(component, 'popupMenu') and component.popupMenu and component.popupMenu.__class__.__name__ == 'JPopupMenu':
				if component.enabled:
					component.selected = True
					component.background = darkGrey
				else:
					component.visible = False
			else:
				component.background = menuItemBGColor
			if not component.enabled or component.__class__.__name__ == 'JLabel':
				component.foreground = black
			else:						
				component.foreground = white

# Handles mouse motion highlighting on lightweight popups that don't trigger a dispatch event
class PopupWindowPainter(MouseAdapter):
	def mouseEntered(self, event):
		if event.source.__class__.__name__ == 'JLabel':
			event.source.background = lightlightGrey
			event.source.opaque = True
			event.source.repaint()
	    
	def mouseExited(self, event):
		if event.source.__class__.__name__ == 'JLabel':
			event.source.background = event.source.parent.background
			event.source.opaque = False
			event.source.repaint()
	
	def mousePressed(self, event):
		pass
	
	def mouseClicked(self, event):
		pass
	
	def mouseReleased(self, event):
		# These are search icons in component pallets
		if event.source.__class__.__name__ == 'JLabel':
			paintPopupWindow(0)
			
		# These are right click window generating components
		elif event.button == event.BUTTON3:
			paintPopupWindow(0)

'''
Property change listener
'''
# In the perspective binding editor, the binding status label will change color depending upon the status of the binding
# These colors need to be lightened while in dark mode to be readable, and this listener accomplishes that
class BindingPreviewListener(PropertyChangeListener):
	def propertyChange(self, event):
		if event.propertyName == 'text':
			if event.newValue in ['Bad_NotFound', 'Error_Configuration']:
				event.source.foreground = system.gui.color('yellow')
			else:
				event.source.foreground = system.gui.color('lightblue')
		if event.propertyName == 'foreground':
			if event.source.text and event.source.text in ['Bad_NotFound', 'Error_Configuration']:
				event.source.foreground = system.gui.color('yellow')
			else:
				event.source.foreground = system.gui.color('lightblue')

# Maintains the background color when certain scenarios could potentially alter it
class BlackBackgroundListener(PropertyChangeListener):
	def propertyChange(self, event):
		if event.propertyName == 'background':
			event.source.background = black
			event.source.foreground = white

# Listens for tag script editor selection changes and undoes any selection triggered restyling of the associated script editor
class ClientTagScriptEditorGuard(PropertyChangeListener):
	def propertyChange(self, event):
		if event.propertyName == 'leadSelectionPath':
			viewport = findComponentOfClass(SwingUtilities.getAncestorOfClass(JSplitPane, event.source), 'PythonTextArea$textArea$1').parent
			setPaintableComponents(viewport, viewport, True)

# Originally created for the (ctrl - f) find/replace window's scrollable labels.
# ...it simply watches the background color during reading changes, and prevents  the dark mode paint from being overwritten
class DarkModeLabelBGListener(PropertyChangeListener):
	def propertyChange(self, event):
		if event.propertyName == 'background' and event.newValue != black:
			event.source.background = black

# Prevents other mouse listeners from disabling the action qualifier panel within the component script editor of Vision
class EnableOverrideListener(PropertyChangeListener):
	def propertyChange(self, event):
		if event.propertyName == 'enabled':
			event.source.enabled = True

# Used in the reporting module's property inspector to color objects that are contiuously blanched by the two JTrees
class OpacityListener(PropertyChangeListener):
	def propertyChange(self, event):
		if event.propertyName == 'opaque' and not event.newValue:
			event.source.opaque = True

# Nested script editors that are subject to jtrees or tabs will often have the default theme reapplied
# ...when switching back and forth between jtree or tab selections
# This listener detects this and corrects the theme
class PythonEditorBGListener(PropertyChangeListener):
	def propertyChange(self, event):
		if event.propertyName == 'RSTA.syntaxScheme' and namedThemeExists and event.source.background != darkScriptEditorTheme.bgColor:
			# Sometimes the gutter color can be missed, so invoke later is used to schedule the theme correction
			# ...after everything else that has been scheduled, eliminating the race condition between the conflicting theme applications
			def applyLater():
				darkScriptEditorTheme.apply(event.source)
			system.util.invokeLater(applyLater)
		
		elif not namedThemeExists and event.propertyName == 'background' and event.newValue != lightGrey:
			event.source.background = lightGrey
			
		
# Used in various JTree components, so the desired colors will stay in place when a user action alters the renderer.
class TreeListener(PropertyChangeListener):
	def __init__(self, backgroundNonSelectionColor, textNonSelectionColor):
		self.backgroundNonSelectionColor = backgroundNonSelectionColor
		self.textNonSelectionColor = textNonSelectionColor
		
	def propertyChange(self, event):
		if event.propertyName == 'cellRenderer':
			event.source.cellRenderer.backgroundNonSelectionColor = self.backgroundNonSelectionColor
			event.source.cellRenderer.textNonSelectionColor = self.textNonSelectionColor
'''
Specialty Listeners
'''
# Prevents other mouse listeners from disabling the action qualifier panel within the component script editor of Vision
class DarkModeSelectionListener(ItemListener):
	def itemStateChanged(self, event):
		if event.stateChange == event.SELECTED:
			event.source.background = darkGrey if getDarkMode() else lightGrey
		else:
			event.source.background = black if getDarkMode() else white

# In the component script editor, Jtree selections and script editing can cause the tab foregrounds to revert,
# This listener wraps the OEM listener that causes this,
# ...retaining its orignal functionality, but  overwriting the undesired behavior
class ScriptBuilderTabRepainter(ItemListener):
	def __init__(self, originalListener, tabbedPane):
		self.originalListener = originalListener
		self.tabbedPane = tabbedPane
		
	def itemStateChanged(self, event):
		self.originalListener.itemStateChanged(event)
		if self.tabbedPane:
			for index in xrange(self.tabbedPane.tabCount):
				if index == self.tabbedPane.selectedIndex: # Selected tab = light blue, everything else = white
					self.tabbedPane.setForegroundAt(index, system.gui.color('lightblue'))
				else:
					self.tabbedPane.setForegroundAt(index, white)

# In the component script editor, Jtree selections and script editing can cause the tab foregrounds to revert,
# This listener wraps the OEM listener that causes this,
# ...retaining its orignal functionality, but  overwriting the undesired behavior
class TreeChangeTabRepainter(TreeModelListener):
	def __init__(self, originalListener, tabbedPane):
		self.originalListener = originalListener
		self.tabbedPane = tabbedPane
		
	def treeNodesChanged(self, event):
		self.originalListener.treeNodesChanged(event)
		if self.tabbedPane:
			for index in xrange(self.tabbedPane.tabCount):
				if index == self.tabbedPane.selectedIndex:
					self.tabbedPane.setForegroundAt(index, system.gui.color('lightblue'))
				else:
					self.tabbedPane.setForegroundAt(index, white)

	def treeNodesInserted(self, event):
		self.originalListener.treeNodesInserted(event)
		
	def treeNodesRemoved(self, event):
		self.originalListener.treeNodesRemoved(event)
		
	def treeStructureChanged(self, event):
		self.originalListener.treeStructureChanged(event)

'''
Dark Mode Renderers
'''
# Used in tag tree components that can have value and data type columns added or removed
# ...to properly maintian hte column color through visibility toggles
class DarkModeColumnModelListener(TableColumnModelListener):
	def columnAdded(self, event):
		self.resetRenderer(event)
	def columnMarginChanged(self, event):
		pass
	def columnMoved(self, event):
		pass
	def	columnRemoved(self, event):
		self.resetRenderer(event)
	def columnSelectionChanged(self, event):
		pass
	def resetRenderer(self, event):
		for column in event.source.columns:
			column.headerRenderer = DefaultTableCellRenderer()
			column.headerRenderer.background = menuItemBGColor
			column.headerRenderer.foreground = white
			if column.cellRenderer.__class__.__name__ == 'DarkModeTagCellRenderer':
				column.cellRenderer = column.cellRenderer.originalRenderer
			if getDarkMode():
				column.cellRenderer = DarkModeTagCellRenderer(column.cellRenderer)

# The isPlafInstalled validation is probably not needed, but was added during a refactor to eliminate Ignition import dependancies
# ...after recievent an email reporting errors with some Ignition imports in a certain base install configurations
if isPlafInstalled:
	
	# Created to add dark mode coloring to various dropdowns throughout the designer
	class DarkModeComboBoxRenderer(ComboListCellRenderer):
		def __init__(self, originalRenderer):
			self.originalRenderer = originalRenderer
		
		def getListCellRendererComponent(self, list, value, index, isSelected, cellHasFocus):
			ComboListCellRenderer.getListCellRendererComponent(self, list, value, index, isSelected, cellHasFocus)
			isDarkMode = getDarkMode()
			if cellHasFocus or isSelected:
				self.background = menuItemBGColor if isDarkMode else defaultSelectionColor
				self.foreground = white if isDarkMode else black
			else:
				self.background = darkGrey if isDarkMode else white
				self.foreground = white if isDarkMode else black
			return self
	
	# Created for the Perspective filtered component pallet
	class DarkModeFilteredPalletRenderer(ComboListCellRenderer):
		def __init__(self, originalRenderer, isDarkMode):
			self.originalRenderer = originalRenderer
			self.isDarkMode = isDarkMode
		
		def getListCellRendererComponent(self, list, value, index, isSelected, cellHasFocus):
			component = self.originalRenderer.getListCellRendererComponent(list, value, index, isSelected, cellHasFocus)
			isDarkMode = self.isDarkMode
			if cellHasFocus or isSelected:
				component.background = menuItemBGColor if isDarkMode else defaultSelectionColor
				component.foreground = white if isDarkMode else black
				for index, subComponent in enumerate(component.components):
					if index == 0:
						subComponent.foreground = white
					else:
						subComponent.foreground = lightGrey
			else:
				component.background = black if isDarkMode else white
				component.foreground = white if isDarkMode else black
				for index, subComponent in enumerate(component.components):
					if index == 0:
						subComponent.foreground = white
					else:
						subComponent.foreground = lightGrey
			return component

# Originally added to paint the "Recently Modified" tables such as are in the script library and named query splash pages
class DarkModeTableCellRenderer(DefaultTableCellRenderer):
	def __init__(self, originalRenderer):
		self.originalRenderer = originalRenderer
		self.isDarkMode = True
	
	def getTableCellRendererComponent(self, table, value, isSelected, hasFocus, row, column):
		component = self.originalRenderer.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column)
		component.border = None
		if isSelected or not self.isDarkMode:
			component.opaque = True
			component.foreground = white if self.isDarkMode else black
		else:
			component.opaque = False
			component.foreground = white
		return component

# Used in the tag tree table to color the property and datatype columns
class DarkModeTagCellRenderer(DefaultTableCellRenderer):
	def __init__(self, originalRenderer):
		self.originalRenderer = originalRenderer
	
	def getTableCellRendererComponent(self, table, value, isSelected, hasFocus, row, column):
		component = self.originalRenderer.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column)
		if isSelected:
			component.background = defaultSelectionColor
		else:
			component.background = lightGrey
		component.foreground = black
		return component

# Created for the Perspective component pallet which is a collection of JTrees
class DarkModePalletRenderer(DefaultTreeCellRenderer):
	def __init__(self, isDarkMode, originalRenderer):
		self.originalRenderer = originalRenderer
		self.isDarkMode = isDarkMode
	
	def getTreeCellRendererComponent(self, tree, value, selected, expanded, leaf, row, hasFocus):
		component = self.originalRenderer.getTreeCellRendererComponent(tree, value, selected, expanded, leaf, row, hasFocus)
		component.opaque = False
		
		# The original renderer is actually a JFrame that contains two labels
		# One label simply holds an icon, and the other label holds the description
		if self.isDarkMode:
			for label in component.components:
				label.foreground = system.gui.color('white')

		else:
			for label in component.components:
				label.foreground = system.gui.color('black')
			
		return component

# IA uses html to render bean properties, and one of the colors they use is black. This renderer switches the black letters to white,
# ...so they will show up against a black background
class DarkModeTreeCellRenderer(DefaultTreeCellRenderer):
	def __init__(self, originalRenderer):
		self.originalRenderer = originalRenderer

	def getTreeCellRendererComponent(self, tree, value, selected, expanded, leaf, row, hasFocus):
		component = self.originalRenderer.getTreeCellRendererComponent(tree, value, selected, expanded, leaf, row, hasFocus)
		darkModeText = component.text.replace("<html><span style='color: black", "<html><span style='color: white") 
		component.text = darkModeText
		return component

# Adds a listener to a component that can trigger a type of lightweight popup that won't be detected by the dispatch event listener
# The listener will detect when a user performs any action that should trigger a popup
def addPopupSourceListener(popupSource):
	if popupSource and 'PopupWindowPainter' not in [listener.__class__.__name__ for listener in popupSource.mouseListeners]:
		popupSource.addMouseListener(PopupWindowPainter())

# Changes the color scheme throughout the designer from light to dark or from dark to light
# ...depending upon whether or not the isDarkMode boolean value is True or False
def applyPatch():
	# Designer window listener
	class DarkModeWindowMonitor(AWTEventListener):
		def eventDispatched(self, event):
			if event.__class__.__name__ == 'WindowEvent' and event.ID == event.WINDOW_OPENED: 
				window = event.window
				
				isDarkMode = getDarkMode()
				# Check if dark mode is selected, and paint the window accordingly
				if isDarkMode is not None:
					setWindowsPainted(window)
			
	# added logic to prevent multiple of the same listener from being inadvertently added
	toolkit = Toolkit.getDefaultToolkit()
	if 'DarkModeWindowMonitor' not in [proxy.listener.__class__.__name__ for proxy in toolkit.AWTEventListeners]:
		toolkit.addAWTEventListener(DarkModeWindowMonitor(), AWTEvent.WINDOW_EVENT_MASK)

	# Iterate through windows and paint them dark or light depending upon the checkbox setting.
	# For an unknown reason, the designer doesn't seem to properly dispose of windows,
	# ...so there are many worthless windows that do not ever need to be painted,
	# ...and slow the script down if they are not filtered out by the visibility properties.
	# Windows that are reused and simply hidden when not in use, are in the speciail windows list.
	# ...These will be painted whether or not they are visible.
	for window in Window.getWindows():
		if window.visible or window.__class__.__name__ in targetList:
			setWindowsPainted(window)
			window.repaint()

# Adds a "Dark Mode" checkbox option to the main designer window's "View" dropdown
def addSelectionBox():
	# If the checkbox already exists, then pass; nothing else needs to be done
	# Otherwise, add the checkbox.
	if not getSelectionCheckbox():
		designerMainWindow = getOpenDesignerWindow('IgnitionDesigner')
		viewMenu = getViewMenu(designerMainWindow)
		darkmodeCheckbox = JCheckBoxMenuItem("Dark Mode")
		darkmodeCheckbox.selected = False
				
		# Add the listener after setting the checkbox, so the patch is not immediately applied
		# Once the patch is applied, it is involved in maintaining both bright and dark modes,
		# ...and the patch's bright mode, is not garanteed to be the same as the OEM's bright mode
		# ...so for team environments where I imagine some users prefer the OEM theme,
		# ...this allows the OEM theme to remain in place until a user explicitly invokes dark mode
		darkmodeCheckbox.addActionListener(DarkModeCheckBoxListener())
		viewMenu.popupMenu.insert(darkmodeCheckbox, 0)

# Returns all nested components of a given class
# container = The object containing nested components to be recursively searched
# className = the __name__ of the class given as a string
def findAllComponentsOfClass(container, className):
	foundComponents = []
	def searchComponents(container, className):
		for component in container.components:
			if component.__class__.__name__ == className:
				foundComponents.append(component)
			searchComponents(component, className)
	if container:
		searchComponents(container, className)
	return foundComponents

# Returns the first nested component of a given class
# container = The object containing nested components to be recursively searched
# className = the __name__ of the class given as a string
def findComponentOfClass(container, className):
	for component in container.components:
		if component.__class__.__name__ == className:
			return component
		else:
			foundComponent = findComponentOfClass(component, className)
			if foundComponent:
				return foundComponent

def flipIcons(iconHolder, isDarkMode): # iconHolders are probably always buttons, but the variable name was made more generic in case something else has icons that need flipped
	'''
	Enabled vs Disabled --> In light mode or dark mode, the enabled icon will be the one with the highest contrast to the background. In the designer environment, 
	... all buttons have the enabled icon on the 'icon' parameter, and the disabled icon on both the 'disabledIcon and 'disabledSelectedIcon' buttons.
	By default, the darkest icon will be the enabled icon because it provides the most contrast with the bright white background, while
	...the lighter icon represents a disabled button because it provides little contrast to the white background and appears dimmer.
	
	In dark mode, the opposite is true. The darker icon blends into the background making appear disabled, and the lighter icon provides high contrast making it appear enabled.
	Therefore, in dark mode, the icons need to be fipped.
	'''

	# Abort the operation if the argument's icon and disabledSelectedIcon parameters are missing the required icon objects
	if not iconHolder.icon or not iconHolder.disabledSelectedIcon:
		return
	
# The icons can't be arbitrarily flipped back and forth because it's possible that something like a heiarchy change or a transition from a docked window to a floating window
	# ...could cause a button to be processed more than once while in the same mode. Therefore, a helper function is used to check each icon to determine which one is lighter,
	# ...and then, the icons are assigned to icon, disabledIcon, and disabledSelectedIcon parameters as needed to meet the requirements of the current presentation mode
	brightestIcon = iconHolder.icon if getIconBrightness(iconHolder, iconHolder.icon) > getIconBrightness(iconHolder, iconHolder.disabledSelectedIcon) else iconHolder.disabledSelectedIcon
	dimestIcon = iconHolder.icon if iconHolder.icon != brightestIcon else iconHolder.disabledSelectedIcon
	
	if isDarkMode:
		iconHolder.icon = brightestIcon
		iconHolder.disabledIcon = dimestIcon
		iconHolder.disabledSelectedIcon = dimestIcon
		for listener in iconHolder.mouseListeners:
			if listener.__class__.__name__ == 'BasicJideButtonListener':
				iconHolder.removeMouseListener(listener)
				iconHolder.addMouseListener(HighlightListener(listener))
	else:
		iconHolder.icon = dimestIcon
		iconHolder.disabledIcon = brightestIcon
		iconHolder.disabledSelectedIcon = brightestIcon
		for listener in iconHolder.mouseListeners:
			if listener.__class__.__name__ == 'HighlightListener':
				iconHolder.removeMouseListener(listener)
				iconHolder.addMouseListener(listener.originalListener)

# Added as a way to remove Ignition class imports that are needed for the conventional SwingUtilities.getAncestorOfClass
# ...in an effort to make the overall script more adapbtible to version and configuration changes
# Recursively searches each parent for a given class name until no parent is found
def getAncestorOfClass(className, component):
	parent = component.parent
	if parent is None:
		return None
	elif parent.__class__.__name__ == className:
		return parent
	else:
		return getAncestorOfClass(className, parent)

# Determines at run time whether or not the user has selected or deselected darkmode
def getDarkMode():
	selectionCheckbox = getSelectionCheckbox()
	if not selectionCheckbox: # If the checkbox hasn't been added
		return False
	elif selectionCheckbox.selected: # If the checkbox is checked
		return True
	else: # If the checkbox is unchecked
		return False

def getIconBrightness(component, icon):
	'''
	Determines how "bright" an icon is by averaging the rgb values (0 to 255) of every pixel in a given icon
	'''
	# Create a graphic representation of the icon using bufferedImage to gain easy access to pixel data
	bufferedImage = BufferedImage(icon.getIconWidth(), icon.getIconHeight(), BufferedImage.TYPE_INT_ARGB)
	graphics = bufferedImage.createGraphics()
	icon.paintIcon(component, graphics, 0, 0)
	graphics.dispose()
	
	# For each pixel, take the average of the rgb values.
	# Then, sum all of those average values, and divide the sum by the total number of pixels[...or volume of the 2D shape in pixels (width * height)]
	averageBrightness = sum((Color(bufferedImage.getRGB(x, y), True).red + 
		Color(bufferedImage.getRGB(x, y), True).green + 
		Color(bufferedImage.getRGB(x, y), True).blue) / 3.0
		for x in range(bufferedImage.width) for y in range(bufferedImage.height)) / (float(bufferedImage.width) * float(bufferedImage.height))
		
	return averageBrightness

def getNodeEditor(node):
	'''
	Checks to see if a given node is the editor itself, and if not,
	...it uses swing utilities to quickly find the parent node that is the editor
	'''
	if node.__class__.__name__ == 'NodeEditor':
		return node
	else:
		return SwingUtilities.getAncestorOfClass(NodeEditor, node)
		
def getOpenDesignerWindow(windowClassName):
	# locate the window by class name and return it
	for window in Window.getWindows():
		if window.visible and window.__class__.__name__ == windowClassName:
			return window
		
def getPopupComponent(window):
	'''
	This gets the container that is parent to the actual popup menu items.
	IA has a variety of classes that they use for this layer, and they are stored in a list called paintedPopups.
	Recursion is used to find it because the depth of this layer within a given window is not taken for granted.
	'''
	for component in window.components:
		componentClass = component.__class__.__name__
		if componentClass in paintedPopups:
			return component			
		else: 
			popup = getPopupComponent(component)
			if popup:
				return popup

def getSelectionCheckbox():
	designerMainWindow = getOpenDesignerWindow('IgnitionDesigner')
	viewMenu = getViewMenu(designerMainWindow)
	if not viewMenu:
		return
	subElements = viewMenu.popupMenu.subElements
	if not subElements:
		return
	if subElements[0].text == 'Dark Mode':
		return subElements[0]

# Recursively search the designer and locate the view dropdown menu
def getViewMenu(window):
	if not window:
		return
	for component in window.components:
		componentClass = component.__class__.__name__
		
		# Skip excluded classes since none of them will contain the view menu anyway,
		# ...and at least one of them is known to be problematic to recursion
		if componentClass in exclusionList:
			continue
		if componentClass =='JMenu' and component.text == 'View':
			return component
		else:
			viewMenu = getViewMenu(component)
			if viewMenu:
				return viewMenu

def paintComponent(component, background, foreground):
	'''
	This is a simple code golfing function, that eliminates one line of code every time both the foreground and background parameters of a component need to changed
	...It probably removes more than a hundred lines of code in this patch
	'''
	component.background = background
	component.foreground = foreground

# Created as a quick and simple patch to fill in unmapped sections of the perspective action editor
def paintItALL(container):
	for component in container.components:
		if component.components and component.opaque:
			if getDarkMode() and component.background.blue > 200:
				paintComponent(component, almostBlack, white)
			elif not getDarkMode() and component.background == almostBlack:
				paintComponent(component, white, black)
		paintItALL(component)

def paintPopupWindow(attempt):
	'''
	Some lightweight popups won't trip the dispatch event that normally triggers window painting.
	Therefore, a listener is added to the components that activate these popups to detect when a user action should result in a popup being created.
	The components that make use of this function are not storing the popup in accessible parameters like componentPopup window. Consequently,
	...there is no clear association between the resultant popup and the popup itself. The result necessitates iterating through the open windows to find the popup
	...which doesn't necessarily appear immediately after being triggered Since some lightweight popups take longer to assemble than others,
	...this function attempts to locate the popup every 25 milliseconds for up to two seconds.
	Once the resultant popup is located, it's handed to the main painting function and processed.
	'''
	componentFound = False
	attempt += 1
	for window in Window.getWindows():
		if window.__class__.__name__ == 'Popup$HeavyWeightWindow':
			component = getPopupComponent(window)
			if component:
				componentFound = True
				setPaintableComponents(component, window, getDarkMode())
				break
	
	if not componentFound and attempt <= 5: # Try repeatedly for up to a quarter second to locate the popup which could be delated in appearing
		system.util.invokeLater(lambda: paintPopupWindow(attempt), 50)

def processElements(popupMenu, isDarkMode):
	'''
	Processes eanch menu item in a given popup to have and maintain the proper appearance in either dark mode or light mode.
	'''
	for element in popupMenu.subElements:
		# Menu items that have submenus will not display their altered background color unless they are selected,
		# ...and all menu items have a listener that sets the selected property of all other menu items to false on mouseentered event
		# To block this behavior, the stock listeners are wrapped, so they can still perform their normal function, but afterwards,
		# ...the outer listener immediately undoes any undesired actions such as deselecting menu items
		if isDarkMode:
			for listener in element.mouseListeners:
				if listener.__class__.__name__ in ['BasicMenuItemUI$Handler', 'BasicMenuUI$Handler']:
					element.removeMouseListener(listener)
					element.addMouseListener(NonDeselectingListener(listener))
		else:
			for listener in element.mouseListeners:
				if listener.__class__.__name__ == 'NonDeselectingListener':
					element.removeMouseListener(listener)
					element.addMouseListener(listener.originalListener)
		
		# Set all menu items that have submenus to selected, so the altered background color will show
		if hasattr(element, 'popupMenu') and element.popupMenu and element.popupMenu.__class__.__name__ == 'JPopupMenu':
			if isDarkMode and not element.enabled:
				element.visible = False
			elif isDarkMode:
				element.selected = True
				paintComponent(element, darkGrey, white)
			else:
				element.visible = True
				element.selected = False
				paintComponent(element, white, black)
			
			processElements(element.popupMenu, isDarkMode)
		
		# For all other components, make sure the enabled vs disabled icons are correct,
		# ...paint the menu item according to the current presentation mode,
		# ...and alter the text color slightly if needed to reflect when the menu item is disabled
		else:
			flipIcons(element, isDarkMode)
			if isDarkMode:
				if element.enabled and element.__class__.__name__ != 'JLabel': 
					paintComponent(element, menuItemBGColor, white)
				else:						
					paintComponent(element, menuItemBGColor, black)
			else:
				if element.enabled:
					paintComponent(element, white, black)
				else:
					paintComponent(element, white, darkGrey)
			if element.__class__.__name__ == 'JLabel':
				element.foreground = black
		element.repaint()
	
	# In Perspective, some of the node editor popups can contain menu items with subcomponents that are not selectable.
	# This is a problem since an item with submenus must remain selected to maintain its color. However,
	# ...since these submenus are not selectable anyway, there is no need for them to exist,
	# ...so the coloring problem is eliminated by simply making them invisible
	# This creates an additional challenge in Perspective, since these popups contain JLabels that seperate menu items by catagory.
	# On occasion every element in a category will be disabled resulting in an empty category and two JLabels sitting on top of each other.
	# This is handled by making a list of all visible items, and if two consecutive items is a JLabel,
	#...the top JLabel [empty category] is hidden. Also, if the last item in the list is a JLabel, 
	# ...This is interpreted as an empty final category, and that JLabel is hidden.
	if popupMenu.__class__.__name__ == 'NodeEditor$MainEditor$NodeContextMenu' and isDarkMode:
		visibleMenuItems = [menuitem for menuitem in popupMenu.components if menuitem.visible]
		maxIndex = len(visibleMenuItems) - 1
		for index in xrange(len(visibleMenuItems)):
			menuitem = visibleMenuItems[index]
			if menuitem.__class__.__name__ == 'JLabel' and index == maxIndex:
				menuitem.visible = False
			elif menuitem.__class__.__name__ == 'JLabel' and visibleMenuItems[index + 1].__class__.__name__ == 'JLabel':
				menuitem.visible = False

# This function adds the checkbox in the view dropdown that adds the dark mode patch,
# ...or toggles back and forth between dark mode and bright mode
def setDarkMode(isDarkMode = False):
	
	# Verify selection checkbox uas been added
	addSelectionBox()
	
	# Get the checkbox, and set its selection property per the user request
	selectionCheckbox = getSelectionCheckbox()
	selectionCheckbox.selected = isDarkMode
	applyPatch()

def setOpacityListeners(component):
	panels = findAllComponentsOfClass(component, 'ScrollablePanel') + findAllComponentsOfClass(component, 'JPanel') + findAllComponentsOfClass(component, 'PieChartConfigFactory$PieChartConfigPanel')
	for panel in panels:
		if 'OpacityListener' not in [listener.__class__.__name__ for listener in panel.propertyChangeListeners]:
			panel.addPropertyChangeListener(OpacityListener())

# Determines which components get painted and when
def setPaintableComponents(window, currentWindow, isDarkMode):
	'''
	This is the main dark or light mode painting function
	'''
	for component in window.components:
		componentClass = component.__class__.__name__
		'''
		Conditions that determine whether or not the current recursion cycle should be abandoned
		'''			
		# No iteration past root containers that are not from windows in the target list,
		# ...or other specifically selected containers that are not to be colored
		if componentClass == 'JRootPane' and component.parent.__class__.__name__ not in targetList:
			continue
		
		# The exclusion list is a list of components that are either not to be colored or are problematic to the script in some way
		elif componentClass in exclusionList:
		
			# Special case: Get the inner JPanel, and process it. The components porperty of the filterablePallet component is write only
			if componentClass == 'FilterablePalette':
				setPaintableComponents(component.getComponent(0), currentWindow, isDarkMode)
			continue
		
		# This recursive sript depends upon being able to read the components property. If this property is write only, the script fails.
		# ...any component with a write only components attribute should be in the exclusion list
		try:
			component.components
		except:
			print 'Add', componentClass, 'to exclusion list. Its components attribute is write only'
			continue
			
		'''
		Conditions that paint components using the generic color lists
		'''
		
		if window.__class__.__name__ in paintedPopups:
			window.repaint()
			processElements(window, isDarkMode)
		
		elif not isDarkMode: # If reverting to light mode, simply paint everything black on a white background
			if componentClass in bwList + abwList + dgwList + lgbList + llgbList:
				if componentClass == 'JideToggleButton' and component.selected:
					paintComponent(component, lightGrey, white)
				else:
					paintComponent(component, white, black)
			
			# The output console's text pane
			if componentClass == 'JTextPane' and getAncestorOfClass('OutputConsole', component) is not None:
				
				# Create an attribute set for the text color
				attributeSet = SimpleAttributeSet()
				StyleConstants.setForeground(attributeSet, black)  # Set the text color to black.
				
				# Apply the attribute set to the entire document
				document = component.getStyledDocument()
				document.setCharacterAttributes(0, document.length, attributeSet, True)
				listeners = document.documentListeners
				for listener in document.documentListeners:
					if listener.__class__.__name__ == 'DarkModeDocumentListener':
						document.removeDocumentListener(listener)
						for oemListener in listener.originalListeners:
							document.addDocumentListener(oemListener)
						
		# If dark mode, paint components according to the list they are in or don't touch them at all if they are not in one of the list
		elif componentClass in bwList:
			# The output console's text pane looks better with almost black
			if componentClass == 'JTextPane' and getAncestorOfClass('OutputConsole', component) is not None:
				paintComponent(component, almostBlack, white)
				
				# Create an attribute set for the text color
				attributeSet = SimpleAttributeSet()
				StyleConstants.setForeground(attributeSet, white)  # Set the text color to white.
				
				# Apply the attribute set to the entire document
				document = component.getStyledDocument()
				document.setCharacterAttributes(0, document.length, attributeSet, True)
				
				# Wrap the OEM listeners with a dark mode listeners to retain OEM console functionality,
				# ...but keep the forground color white
				listeners = document.documentListeners
				if 'DarkModeDocumentListener' not in [listener.__class__.__name__ for listener in listeners]:
					for listener in document.documentListeners:
						document.removeDocumentListener(listener)				
					document.addDocumentListener(DarkModeDocumentListener(listeners))
			
			elif componentClass == 'JideToggleButton' and component.selected:
				paintComponent(component, darkGrey, white)
			else:
				paintComponent(component, black, white)
		elif componentClass in abwList:
				paintComponent(component, almostBlack, white)
		elif componentClass in dgwList:
			paintComponent(component, darkGrey, white)
		elif componentClass in lgbList:
			paintComponent(component, lightGrey, black)
			if hasattr(component, 'font') and component.font:
				try:
					component.font = component.font.deriveFont(component.font.BOLD)
				except:
					pass
				
		elif componentClass in llgbList:
			paintComponent(component, lightlightGrey, black)

		# BorderlessField, ComponentScopeEditor$BindingCompatibleNodeEditor$2, InteractionLayer, NodeEditor$MainEditor, NodeEditor$MainEditor$1, PerspectiveKeyEditor, TagFrameTree
		# These components can trigger a popup window. These lightweight popups can't be detected by the dispatched event listener,
		# ...so a special listener is added to detect the popup and subsequently paint it.
		elif componentClass in heavyWeightPopupListenerList:
			addPopupSourceListener(component)
		
		else:
			pass

		'''
		Conditions for giving certain components special treatment
		'''
		# AbstractBrowsableGalleryPanel$SearchField, CollapsiblePanePalette$2, NavTreePanel$NavTreeFilterField, QuickTableFilterField
			# These components contain a JLabel that can trigger a popup window. These lightweight popups can't be detected by dispatched event listener,
			# ...so a special listener is added to the JLabel to detect the popup and subsequently paint it.
		if componentClass in ['AbstractBrowsableGalleryPanel$SearchField', 'CollapsiblePanePalette$2', 'NavTreePanel$NavTreeFilterField', 'QuickTableFilterField']:
			
			# The JLabel is a subcomponent that has to be located in this way because to ensure this code continues to work even if the label's index in the subheiarchy changes
			popupSource = next(iter([label for label in component.components if label.__class__.__name__ == 'JLabel']), None)
			addPopupSourceListener(popupSource)
		
		elif componentClass in ['ActionEditPanel', 'ScriptEditorFrame$2']:
			paintItALL(component)
		
		# ActionQualPanel
			# This component doesn't look good in dark mode in its disabled state, and the outer panel being enabled doesn't effect the disabled internal components
			# ...so a property change listener is added to prevent other listeners from disabling the panel while in dark mode
		elif componentClass == 'ActionQualPanel':
			component.enabled = True
			if isDarkMode:
				if 'EnableOverrideListener' not in [listener.__class__.__name__ for listener in component.propertyChangeListeners]:
					component.addPropertyChangeListener(EnableOverrideListener())
			else:
				for listener in component.propertyChangeListeners:
					if listener.__class__.__name__ == 'EnableOverrideListener':
						component.removePropertyChangeListener(listener)
		
		# AntialiasLabel
			# Used in collapsible dropdowns such as the description dropdown in the extension function editor of the Vision component script editor window
			# Not all Antialiaslabels should be arbitrarily painted, so this is done in a seperate operation
		elif componentClass == 'AntialiasLabel' and 'CollapsiblePane$a' == component.parent.__class__.__name__:
			if isDarkMode:
				paintComponent(component, black, white)
				component.opaque = True # Opacity for this component is specific to the above conditions
			else:
				paintComponent(component, white, black)
				component.opaque = False
		
		elif componentClass == 'JLabel' and component.parent.__class__.__name__ == 'ActionEditPanel':
			if isDarkMode:
				paintComponent(component, black, white)
			else:
				paintComponent(component, white, black)

		# Perspective component script and event handlser windows
		elif componentClass == 'AntialiasLabel' and (component.text in ['Events', 'Scripts'] or component.parent.parent.__class__.__name__ == 'ActionCollectionEditor'):
			if isDarkMode:
				paintComponent(component, black, white)
			else:
				paintComponent(component, white, black)
		
		# Factory Menu Editor
		elif componentClass == 'AutoscrollingJTree' and getAncestorOfClass('MenuEditor', component):
			setScriptEditorGuard(component, isDarkMode)
				
		# BannerPanel$1
			# It's light mode color is non-generic, so it's coloring is handled outside the generic lists
		elif componentClass == 'BannerPanel$1': # Found in the Vision binding editor's no binding banner
			component.foreground = lightlightGrey if isDarkMode else darkGrey
		
		# BindingEditor$PreviewPanel$PreviewLabel$1
			# This is a label in the binding preview area of the Perspective binding editor. It displays the status of a binding,
			# ...and is color coded. The colors need to be lightened for dark mode to create better contrast, so that is done here,
			# ...and while in dark mode, a listener is added to maintain the lighter colors when a user action causes the status label to change states
		elif componentClass == 'BindingEditor$PreviewPanel$PreviewLabel$1':
			if isDarkMode:
				if component.text in ['Bad_NotFound', 'Error_Configuration']:
					component.foreground = system.gui.color('yellow')
				else:
					component.foreground = system.gui.color('lightBlue')
					
				if 'BindingPreviewListener' not in [listener.__class__.__name__ for listener in component.propertyChangeListeners]:
					component.addPropertyChangeListener(BindingPreviewListener())
			else:
				for listener in component.propertyChangeListeners:
					if listener.__class__.__name__ == 'BindingPreviewListener':
						component.removePropertyChangeListener(listener)
				if component.text in ['Bad_NotFound', 'Error_Configuration']:
					component.foreground = system.gui.color('red')
				else:
					component.foreground = system.gui.color('blue')
		
		# ChartPanel
			# Found in the diagnostic popup's performance tab
		elif componentClass == 'ChartPanel': 
			component.chart.plot.backgroundPaint = lightGrey if isDarkMode else white
		
		# There are two JLabels in the container. One has a text property with a value 'Search' or 'Filter, and the other has an icon
		elif componentClass in ['ComponentPaletteFilterField', 'PropertyEditorFrame$1']:
			jLabel = [label for label in findAllComponentsOfClass(component, 'JLabel') if label.icon][0]
			addPopupSourceListener(jLabel)

		# DataPanel$DataListCellRenderer, DataPanel$GroupCellRenderer
			# These are a special cases where the SyntheticaSafeGroupList background should be light grey instead of black
		elif componentClass in ['DataPanel$DataListCellRenderer', 'DataPanel$GroupCellRenderer']:
			getAncestorOfClass('SyntheticaSafeGroupList', component).background = lightGrey

		elif isPlafInstalled and componentClass == 'FilterablePalette$2':
			component.background = black
			if component.cellRenderer.__class__.__name__ != 'DarkModeFilteredPalletRenderer':
				originalRenderer = component.cellRenderer
				component.cellRenderer = DarkModeFilteredPalletRenderer(originalRenderer, isDarkMode)
			else:
				component.cellRenderer.isDarkMode = isDarkMode

		# IconButton
			# Unlike other buttons in the designer, the icon button's color is determined by its foreground property,
			# ...and it comes with a mouse listener that alters that color when the mouse enters and exits to produce a highlight effect.
			# Therefore, to keep the color consistant with the dark mode theme, its mouse listener is wrapped,
			# ...and the OEM mouse listener's coloring behavior is overwritten while in dark mode
		elif componentClass == 'IconButton':
			if isDarkMode:
				for listener in component.mouseListeners:
					if listener.__class__.__name__ == 'IconButton$1':
						component.removeMouseListener(listener)
						component.addMouseListener(IconSaverListener(listener))
			else:
				for listener in component.mouseListeners:
					if listener.__class__.__name__ == 'IconSaverListener':
						component.removeMouseListener(listener)
						component.addMouseListener(listener.originalListener)

		# IndirectTagBindingConfigurator$RefTable
			# Digs a table header out of the embedded table, and properly paints it according to the current presentation mode
		elif componentClass == 'IndirectTagBindingConfigurator$RefTable':
			scrollPane = findComponentOfClass(component, 'JScrollPane')
			if scrollPane:
				for column in scrollPane.viewport.view.columnModel.columns:
					if isDarkMode:
						column.headerRenderer = DefaultTableCellRenderer()
						column.headerRenderer.background = menuItemBGColor
						column.headerRenderer.foreground = white
					else:
						column.headerRenderer = None

		# InspectorFrame$CustomPropertyTable, PropertyTablePanel$CustomPropertyTable
			# These tables have a special area that creates a collapsible nested sub property effect
			# This special area is colored using the marginBackground property
		elif componentClass in ['InspectorFrame$CustomPropertyTable', 'PropertyTablePanel$CustomPropertyTable']:
			if isDarkMode:
				component.marginBackground = lightGrey
				component.background = lightlightGrey
			else:
				component.marginBackground = white

		# JButton
			# Special dark mode cases where the color of the JButton need to be non-standard for optimal appearance
		elif componentClass == 'JButton' and isDarkMode:
			if component.text == 'Execute' and getAncestorOfClass('QueryBrowser', component):
				component.background = almostBlack
				component.foreground = lightGrey
			
			elif component.text == 'Project Properties':
				component.foreground = lightlightGrey
		
		# JCheckBox
			# This is a special case where a JCkecBox can trigger a lightweight popup window that can't be detected by the dispatched event listener,
			# ...so a special listener is added to detect the popup and subsequently paint it.
		elif componentClass == 'JCheckBox' and component.parent.__class__.__name__ == 'ComponentScopeEditor$BindingCompatibleNodeEditor$2':
			addPopupSourceListener(component)
		
		# JComboBox, TagToolbar$ProviderDropdown
			# The TagToolbar$ProviderDropdown behaves well with adding and removing the DarkModeComboBoxRenderer,
			# ...but it doesn't behave as expected in light mode if the original renderer isn't put back in place
			# The NavigationBuilder$WrappingToolTipListCellRenderer class lock up the script editor with DarkModeComboBoxRenderer,
			# ...and to that end, they seem to be doing something that is color dependant, so these comboboxes are entirely left alone
			# The new view dialog window does not render the correct text when DarkModeComboBoxRenderer is used
		elif isPlafInstalled and componentClass in ['JComboBox', 'TagToolbar$ProviderDropdown'] and component.renderer.__class__.__name__ not in ['NavigationBuilder$WrappingToolTipListCellRenderer', 'NewViewDialog$5']:
			if isDarkMode and component.renderer.__class__.__name__ != 'DarkModeComboBoxRenderer':
				component.renderer = DarkModeComboBoxRenderer(component.renderer)
			elif not isDarkMode and component.renderer.__class__.__name__ == 'DarkModeComboBoxRenderer':
				component.renderer = component.renderer.originalRenderer
			
		# JFormattedTextField, JTextField, JSpinner$NumberEditor
			# The foregrounds change in this window, but backgrounds do not change for these components. 
		elif componentClass in ['JFormattedTextField', 'JTextField', 'JSpinner$NumberEditor']:# and currentWindow.__class__.__name__ in ['SwingBorderEditor$BorderDialog', 'PropertyEditorDialog']:
			component.foreground = black
		
		# JideButton
			# Special Cases
			# ...added lower() to validation because inconsistant capitalization practices between modules could forseeably be rectified or changed in a future Ignition version
		elif componentClass == 'JideButton' and component.text and ('Open ' in component.text or component.text == 'Default' or 'provider' in component.text.lower() or 'all groups' in component.text.lower()):
			component.foreground = defaultHighlightColor if isDarkMode else black # Find replace instances
		elif componentClass == 'JideButton' and component.text in ['Save', 'Edit Script']:
			component.foreground = lightlightGrey if isDarkMode else black
			component.background = white if isDarkMode else lightlightGrey
		elif componentClass == 'JideButton':
			component.background = white if isDarkMode else lightlightGrey
		
		# This was originally handled with the HighlightListener mouse adapter, but the selections can changed based on what component is clicked on within the Vision editor,
		# ...so simply changing the selected colors based purely on mouse selection is insufficient. This creates some overlap in selection coloring,
		# ...that could possibly be made cleaner by creating a seperate class of mouse listener for the JideToggleButtons.
		elif componentClass == 'JideToggleButton' and 'DarkModeSelectionListener' not in [listener.__class__.__name__ for listener in component.itemListeners]:
				component.addItemListener(DarkModeSelectionListener())
		
		#JLabel
			# JLabels had to be isolated from the standard bwlist because, for unknown reasons,
			# ...inheritable NavTree text reverts to white foregrounds instead of grey regardless of light or dark mode
			# ...making them impossible to see in light mode
		elif componentClass == 'JLabel':
			# This node editor can generate a lightweight popup that is undetectable by the event dispatched listener,
			# ...so a special listener has to be added to ensure the popup is properly painted
			if component.parent.__class__.__name__ == 'NodeEditor$MainEditor':
				addPopupSourceListener(component)
			
			# The NavTreePanel jlabels can't be directly touched, or the labels that represent inheritancy become invisible [the same color as the background] in light mode
			if not getAncestorOfClass('NavTreePanel', component) and not getAncestorOfClass('AutoscrollingJTree', component):
				if isDarkMode:
					paintComponent(component, black, white)
				else:
					paintComponent(component, white, black)
				
				# The InlineTipLabel container needs a black foreground at all times
				if component.parent.__class__.__name__ == 'InlineTipLabel':
					component.foreground = black
				
		#JRadioButton
			# In the component script editor, there are certain listeners that will cause the tab foreground colors to revert to light mode.
			# The script builder listeners that are triggered by various radio buttons within the window do this. Therefore, these listeners must be wrapped, 
			# ...so any color changes they impose while performing their script building function will be overwritten
		elif componentClass == 'JRadioButton' and currentWindow.__class__.__name__ == 'ComponentScriptEditor':
			if isDarkMode:
				for listener in component.itemListeners:
					if 'builder' in listener.__class__.__name__.lower():
						component.model.addItemListener(ScriptBuilderTabRepainter(listener, findComponentOfClass(currentWindow, 'JTabbedPane')))					
			else:
				for listener in component.itemListeners:
					if listener.__class__.__name__ == 'ScriptBuilderTabRepainter':
						component.model.removeTreeModelListener(listener)
						component.model.addTreeModelListener(listener.originalListener)
		
		# JTree
			# The JTree$TreeModelHandler is a listener on the JTree component of the component script editor window
			# ...that will cause the text on the tabs in the scripting pane to revert back to their light mode colors,
			# ...so in dark mode, the listener is wrapped, and its color changing behavior is subsequently overwritten
		elif componentClass == 'JTree' and currentWindow.__class__.__name__ == 'ComponentScriptEditor':
			setScriptEditorGuard(component, isDarkMode)
			if isDarkMode:
				for listener in component.model.treeModelListeners:
					if listener.__class__.__name__ == 'JTree$TreeModelHandler':
						component.model.addTreeModelListener(TreeChangeTabRepainter(listener, findComponentOfClass(currentWindow, 'JTabbedPane')))
			else:
				for listener in component.model.treeModelListeners:
					if listener.__class__.__name__ == 'TreeChangeTabRepainter':
						component.model.removeTreeModelListener(listener)
						component.model.addTreeModelListener(listener.originalListener)
				
		# This JTree somehow overwrites the styling in the python text area, so a watchdog listener is added to it to undo its style changes before the user can evem see them
		elif (componentClass == 'JTree' and getAncestorOfClass('TagObjectEditor', component)) or (componentClass == 'NestedTooltipAwareJTree' and getAncestorOfClass('TagEditorDialog', component)):
			setScriptEditorGuard(component, isDarkMode)
		
		# LocaleCheckboxList
			# The localeCheckBoxList uses a jidesoft checkBoxListRenderer, but adding a stock custom creates two checkboxes.
			# ...A Combo listener works as expected, but replacing it with the original when switching back to light mode resulted in unexpected behavior
			# ...Therefore, with regard to the LocaleCheckboxList, the supplied renderer is a one and done, with all behaviors built in.
		elif isPlafInstalled and componentClass == 'LocaleCheckboxList':
			if component.cellRenderer.__class__.__name__ != 'DarkModeComboBoxRenderer':
				component.cellRenderer = DarkModeComboBoxRenderer(component.cellRenderer)
		
		# PalletItem
			# Perspective component pallet item [JTree containing a rendered JPanel with two labels: one for an the icon and one for the text]
		elif componentClass == 'PaletteItem':
			if component.cellRenderer.__class__.__name__ == 'PaletteItem$CellRenderer':
				if isDarkMode:
					component.background = black
				else:
					component.background = white
				component.cellRenderer = DarkModePalletRenderer(isDarkMode, component.cellRenderer)
				
			elif component.cellRenderer.__class__.__name__ == 'DarkModePalletRenderer':
				if isDarkMode:
					component.background = black
					component.cellRenderer.isDarkMode = True
				else:
					component.background = white
					component.cellRenderer.isDarkMode = False
		
		# RecentlyModifiedTablePanel$1
			# Known to exist in the library script and named query splash pages
		elif componentClass == 'RecentlyModifiedTablePanel$1':
			# When in dark mode, make the table black with a white foreground, and make the selected row the menuItem color
			component.background = black if isDarkMode else white
			component.foreground = white if isDarkMode else black
			component.selectionBackground = menuItemBGColor if isDarkMode else defaultSelectionColor
			component.selectionForeground = white if isDarkMode else black
			component.showVerticalLines = True if isDarkMode else False
			
			# Prior to 8.1.3x the opacity of the table was true, this line was added to improve the presentation of latter versions
			component.opaque = True if isDarkMode else False
			
			# Wrap the default cell renderer to maintain the proper colors, even after switching to bright mode
			for column in xrange(component.columnCount):
				renderer = component.getDefaultRenderer(component.getColumnClass(column))
				if not isDarkMode and renderer.__class__.__name__ == 'DarkModeTableCellRenderer':
					renderer.isDarkMode = False
				elif component.getDefaultRenderer(component.getColumnClass(column)).__class__.__name__ == 'DarkModeTableCellRenderer':
					renderer.isDarkMode = True
				else:	
					component.setDefaultRenderer(component.getColumnClass(column), DarkModeTableCellRenderer(component.getDefaultRenderer(component.getColumnClass(column))))
		
		#ResourceBuilderPanel$CreateResourceTile
			# Wrap the mouse listener for resource bulder tiles to control mouseover actions
			# Class 'ResourceBuilderPanel$CreateResourceTile' = Main Window, Popup Window, Docked Window, etc; These are the tiles on the primary Vision preview tab
		elif componentClass == 'ResourceBuilderPanel$CreateResourceTile':
			for listener in component.mouseListeners:
				if listener.__class__.__name__ == 'HighlightListener':
					component.removeMouseListener(listener)
					component.addMouseListener(listener.originalListener)
			if isDarkMode:
				for listener in component.mouseListeners:
					component.removeMouseListener(listener)
					component.addMouseListener(HighlightListener(listener))
				if component.background.red > 230 or component.background == lightGrey:
					component.background = lightGrey
				else:
					component.background = black
			else:
				if component.background.red > 0:
					component.background = system.gui.color(235, 239, 242) # OEM deselected background RGB
				else:
					component.background = system.gui.color(221, 229, 235) # OEM selected background RGB
				
		# RTextScrollPane
			# Add the special listeners needed to the scripting areas to ensure they display correctly while in dark mode
			# The real reason for the listeners is the Vision component script area that changes the RSTA.syntaxTheme after the theme is initially applied.
		elif isDarkMode and componentClass in ['PythonTextArea$textArea$1', 'RSyntaxTextArea']:
			if namedThemeExists:
				darkScriptEditorTheme.apply(component)
			else:
				component.background = lightGrey
				if 'PythonEditorBGListener' not in [listener.__class__.__name__ for listener in component.propertyChangeListeners]:
					component.addPropertyChangeListener(PythonEditorBGListener())
		elif not isDarkMode and componentClass in ['PythonTextArea$textArea$1', 'RSyntaxTextArea']:
			for listener in component.propertyChangeListeners:
				if listener.__class__.__name__ == 'PythonEditorBGListener':
					component.removePropertyChangeListener(listener)
			if namedThemeExists:
				lightScriptEditorTheme.apply(component)
			else:
				component.background = white
		
		# ScriptEditorBuilder
			# The script text area looses dark mode when the tabs are changed from some other tab to the script editor tab.
			# Consequently, a listener is added to detect when the tab is selected, so the text area can be repainted with the appropriate theme
		elif componentClass == 'ScriptEditorBuilder' and 'TabVisibilityListener' not in [listener.__class__.__name__ for listener in component.ancestorListeners]:
			component.addAncestorListener(TabVisibilityListener())
			
		
		# SimpleTreeTable
		elif componentClass == 'SimpleTreeTable':
			if not isDarkMode:
				for listener in component.viewport.view.columnModel.columnModelListeners:
					if listener.__class__.__name__ == 'DarkModeColumnModelListener':
						component.viewport.view.columnModel.removeColumnModelListener(listener)
				component.background = white
			elif 'DarkModeColumnModelListener' not in [listener.__class__.__name__ for listener in component.viewport.view.columnModel.columnModelListeners]:
				component.viewport.view.columnModel.addColumnModelListener(DarkModeColumnModelListener())
				component.background = lightGrey
			
			for column in component.viewport.view.columnModel.columns:
				if not isDarkMode and column.cellRenderer.__class__.__name__ == 'DarkModeTagCellRenderer':
					column.cellRenderer = column.cellRenderer.originalRenderer
					column.headerRenderer = None
				elif isDarkMode and column.cellRenderer.__class__.__name__ != 'DarkModeTagCellRenderer':
					column.cellRenderer = DarkModeTagCellRenderer(column.cellRenderer)
					column.headerRenderer = DefaultTableCellRenderer()
					column.headerRenderer.background = menuItemBGColor
					column.headerRenderer.foreground = white
		
		# SortableTable
			# This is the tabel in the (ctrl - f) find/replace window: Slighyly color it, so it isn't so bright
		elif componentClass == 'SortableTable':
			if getAncestorOfClass('SearchReplaceDialog', component):
				component.background = lightlightGrey if isDarkMode else white
				component.foreground = white if isDarkMode else black
				component.selectionBackground = menuItemBGColor if isDarkMode else defaultSelectionColor
				component.selectionForeground = white if isDarkMode else black
				component.showVerticalLines = True if isDarkMode else False
				component.opaque = True if isDarkMode else False

			elif getAncestorOfClass('ResultTable', component):
				component.background = black if isDarkMode else white
				component.foreground = black
		
		# StandardBannerPanel
		# The buttons and the tag editor panel look weird because the background occasionally gets overwritten
		# A generic listener is used to maintain the properyies as needed.
		elif componentClass == 'StandardBannerPanel' and currentWindow.__class__.__name__ == 'TagEditorDialog':
			bannerPanelComponents = [component] + findAllComponentsOfClass(component, 'JButton') + findAllComponentsOfClass(component, 'JToggleButton') + findAllComponentsOfClass(component, 'JPanel')
			if isDarkMode:
				for bannerPanelComponent in bannerPanelComponents:
					bannerPanelComponent.background = black
					if 'BlackBackgroundListener' not in [listener.__class__.__name__ for listener in bannerPanelComponent.propertyChangeListeners]:
						bannerPanelComponent.addPropertyChangeListener(BlackBackgroundListener())
			else:
				for bannerPanelComponent in bannerPanelComponents:
					for listener in bannerPanelComponent.propertyChangeListeners:
						if listener.__class__.__name__ == 'BlackBackgroundListener':
							bannerPanelComponent.removePropertyChangeListener(listener)
					
					# Change the background color to white only after the listener has been removed
					bannerPanelComponent.background = white 
					
		# TagDialogHeader
			# The parent jpanel for this component needs to be light grey
		elif componentClass == 'TagDialogHeader':
			if isDarkMode:
				component.parent.background = lightGrey
			else:
				component.parent.background = white
			component.parent.repaint()
		'''
		Additional cross componentClass processing
		'''
		# Cell Rendering
			# Change the color scheme of any component that has a cell renderer, and add a listener to maintain it
		if hasattr(component, 'cellRenderer') and component.cellRenderer:
			cellRenderer = component.cellRenderer
			if hasattr(cellRenderer, 'backgroundNonSelectionColor') and hasattr(cellRenderer, 'textNonSelectionColor'):
				if not isDarkMode:
					component.background = white
					
					# Apply to whatever renderer the component has in bright mode
					cellRenderer.backgroundNonSelectionColor = white
					cellRenderer.textNonSelectionColor = black
					if cellRenderer.__class__.__name__ == 'DarkModeTreeCellRenderer':
						cellRenderer = component.cellRenderer.originalRenderer
						component.cellRenderer = cellRenderer
						
						# NOT REDUNDANT! # While these two lines are repeated above and below the if statement, below the if statement is a transition occurance,
						# ...and above the if statement is all post transitional occurances
						# Set the colors back specifically to the original renderer after the dark mode renderer has been removed
						cellRenderer.backgroundNonSelectionColor = white
						cellRenderer.textNonSelectionColor = black
					
				elif cellRenderer.__class__.__name__ in ['ComponentScriptEditor$Renderer', 'TagEventCategory$Renderer', 'EventScriptEditor$Renderer']:
					component.background = lightGrey
					cellRenderer.backgroundNonSelectionColor = lightGrey
					cellRenderer.textNonSelectionColor = black
				
				elif cellRenderer.__class__.__name__ == 'BeanCellRenderer':
					component.background = black
					cellRenderer.backgroundNonSelectionColor = black
					cellRenderer.textNonSelectionColor = white
					darkCellRenderer = DarkModeTreeCellRenderer(cellRenderer)
					component.cellRenderer = darkCellRenderer
				
				else:
					component.background = black
					cellRenderer.backgroundNonSelectionColor = black
					cellRenderer.textNonSelectionColor = white
				
				if not isDarkMode:
					for listener in component.propertyChangeListeners:
						if listener.__class__.__name__ == 'TreeListener':
							component.removePropertyChangeListener(listener)
				elif 'TreeListener' not in [listener.__class__.__name__ for listener in component.propertyChangeListeners]:
					component.addPropertyChangeListener(TreeListener(cellRenderer.backgroundNonSelectionColor, cellRenderer.textNonSelectionColor))
		
		# Checkbox and Transparent background button handling
			# Handled outside the standard component color lists, so the background of the checkbox will be white
		if componentClass in ['TristateCheckBox', 'JCheckBox', 'JRadioButton']:
			component.background = white # The background color effects the visibility of the checkbox
			component.foreground = white if isDarkMode else black # Maximize text contrast
			component.opaque = False # Allows the non checkbox background to simply be the parent container's background color

		# Container Listeners
			# Add a container listener to every container type in the designer to detect when items are added,
			# ...so those items can be painted to the current color scheme
		
		# criteria for exclusion
		isContainer = component.components or componentClass in specialContainerList
		for partialClassName in ['configurator', 'container', 'dialog', 'frame', 'menu', 'panel']:
			if isContainer:
				break
			elif partialClassName in componentClass.lower():
				isContainer = True
				break
		
		excludedParentList = ['CellRendererPane', 'ErrorStrip', 'TagRenderer'] # During a listener audit, these component classes were found to not only not be needed, but also to be capable of creating an absurd amount of inefficency
		notRenderer = 'renderer' not in componentClass.lower()
		existingListeners = [listener.__class__.__name__ for listener in component.containerListeners]
		
		if isContainer and componentClass not in excludedParentList and not 'DarkModeContainerListener' in existingListeners and notRenderer:
			component.addContainerListener(DarkModeContainerListener())
		
		# Icon Flipping
			# Components with seperate enabled and disabled icons, need to have those icons reversed in dark mode,
			# since it is higher contrast that makes a icon look inabled. Light colors don't show up as well aginst white backgrounds, so they looked broken or disabled,
			# However, light colors stand out against a dark background, and it is the darker colors that blend in and consequently look disabled.
		if componentClass in iconFlipList and all(iconClass == 'VectorIcon' for iconClass in [component.disabledIcon.__class__.__name__, component.disabledIcon.__class__.__name__, component.disabledSelectedIcon.__class__.__name__]):
			flipIcons(component, isDarkMode)			
		elif componentClass == 'CommandBar$a' and all(iconClass == 'ImageIconUIResource' for iconClass in [component.disabledIcon.__class__.__name__, component.disabledIcon.__class__.__name__, component.disabledSelectedIcon.__class__.__name__]):
			flipIcons(component, isDarkMode)
		
		# Opacity processing [Processed after the main evaluation]
			# Some components require opacity to be reversed for dark mode in order to diplay correctly,
			# ...if their container background is different in dark mode than the desired component background
		if componentClass in ['Box', 'Box$Filler'] and component.parent.__class__.__name__ in ['CollapsiblePanes', 'BorderChooser']:
			# Special case. When using the collapsable panes search box filter. the bottom of the pane becomes white.
			component.opaque = True # Always True for this specific instance
		elif isDarkMode:
			if componentClass == 'JPanel' and component.parent.__class__.__name__ == 'JRootPane': # This Jpanel is special and involved in moving dockable windows
				pass
			elif componentClass in ['JPanel', 'PieChartConfigFactory$PieChartConfigPanel', 'ScrollablePanel']:
				inspectorFrame = getAncestorOfClass('InspectorFrame', component)
				if inspectorFrame:
					setOpacityListeners(inspectorFrame)
				component.opaque = True
			elif componentClass in ['JPanel', 'PieChartConfigFactory$PieChartConfigPanel', 'ScrollablePanel']:
				component.opaque = True
			elif componentClass in darkModeOpacityList:
				component.opaque = True
			elif componentClass in darkModeTransparencyList:
				component.opaque = False
			if componentClass == 'ImageBrowser':
				for subComponent in component.components:
					if subComponent.__class__.__name__ == 'JLabel' and subComponent.text and 'Tip' in subComponent.text:
						subComponent.opaque = True
		else:
			if componentClass in ['JPanel', 'PieChartConfigFactory$PieChartConfigPanel', 'ScrollablePanel']:
				for listener in component.propertyChangeListeners:
					if listener.__class__.__name__ == 'OpacityListener':
						component.removePropertyChangeListener(listener)
			if componentClass == 'JPanel' and component.parent.__class__.__name__ == 'JRootPane': # This Jpanel is special and involved in moving dockable windows
				pass
			elif componentClass in darkModeOpacityList:
				component.opaque = False
			elif componentClass in darkModeTransparencyList:
				component.opaque = False
			
		# Node Editor Processing
			# Colors nodes and adds highlight listener to JSON node editors such as the one in the right pane of the keyboard manager
		if isJsonEditInstalled and (componentClass == 'NodeEditor' or SwingUtilities.getAncestorOfClass(NodeEditor, component)):
			for listener in component.mouseListeners:
				if listener.__class__.__name__ == 'DarkModeNodeHighlighter':
					component.removeMouseListener(listener)
					if listener.originalListener is not None:
						component.addMouseListener(listener.originalListener)
			
			if isDarkMode:
				hoverListenerFound = False
				for listener in component.mouseListeners:
					if listener.__class__.__name__ == 'HoverTracker$ComponentTracker':
						component.removeMouseListener(listener)
						component.addMouseListener(DarkModeNodeHighlighter(listener, getNodeEditor(component)))
						hoverListenerFound = True
				
				# Sometimes the regular hover listener that does the highlighting doesn't get added right away, 
				# ...so add the dark mode listener no matter what, and use it to collect the missing listener later
				if not hoverListenerFound:
					component.addMouseListener(DarkModeNodeHighlighter(None, getNodeEditor(component)))
					
				if componentClass == 'BorderlessField':
					component.background = almostBlack
				else:
					component.background = black
				component.foreground = white
			
			else:
				if componentClass == 'BorderlessField':
					component.background = lightlightGrey
				else:
					component.background = white
				component.foreground = black

		# Popup menu processessing
			# If a popup menu is detected in a component property, send its popupmenu to the processElements function
			# ...to paint the elements, add the necessary listeners, and process any subelements that are present
		if hasattr(component, 'popupMenu') and component.popupMenu and component.popupMenu.__class__.__name__ == 'JPopupMenu':
			processElements(component.popupMenu, isDarkMode)
		
		if hasattr(component, 'border') and hasattr(component.border, 'title') and component.border.title:
			if useLightForeground(component.background):
				component.border.titleColor = white
			else:
				component.border.titleColor = black
		
		# (ctrl - f) find/replace window target border doesn't change at initialization like other titled borders due to the way it's nested
		if componentClass == 'JScrollPane' and component.border and hasattr(component.border, 'title') and component.border.title == 'Target':
			component.border.titleColor = white if isDarkMode else black
		
		# Add a listener to the find and replace scrollable lables so their colors don't blip between table selections
		if componentClass == 'JRootPane' and component.parent.__class__.__name__ == 'SearchReplaceDialog':
			labels = [pane.viewport.view for pane in findAllComponentsOfClass(component, 'JScrollPane') if pane.viewport.view.__class__.__name__ == 'JLabel']
			for label in labels:
				if isDarkMode and 'DarkModeLabelBGListener' not in [listener.__class__.__name__ for listener in label.propertyChangeListeners]:
					label.addPropertyChangeListener(DarkModeLabelBGListener())
				elif not isDarkMode:
					for listener in label.propertyChangeListeners:
						if listener.__class__.__name__ == 'DarkModeLabelBGListener':
							label.removePropertyChangeListener(listener)
		
		# Call the processed components repaint event to paint any changes,
		# ...and pass the component recursively back into the setPaintableComponents function to process any subComponents
		component.repaint()
		setPaintableComponents(component, currentWindow, isDarkMode)

def setScriptEditorGuard(component, isDarkMode):
	if isDarkMode:
		if 'ClientTagScriptEditorGuard' not in [listener.__class__.__name__ for listener in component.propertyChangeListeners]:
			component.addPropertyChangeListener(ClientTagScriptEditorGuard())
	else:
		for listener in component.propertyChangeListeners:
			if listener.__class__.__name__ == 'ClientTagScriptEditorGuard':
				component.removePropertyChangeListener(listener)

# targetClass allows of specialization of subcomponents where needed
# Controls how and when window subcomponents are painted
def setWindowsPainted(window):
	
	# A static variable that allows a reference to the starting point in the nested recursive function
	currentWindow = window
	
	# Get te up to date dark mode
	isDarkMode = getDarkMode()
	
	# Call the recurstive nested function that paints everything inside a given window
	setPaintableComponents(window, currentWindow, isDarkMode)

	# Checks the brightness of a given color using weighted RGB values,
	# ...and if the brightness exceeds a certain threshold, black is returned else white
def useLightForeground(background):
	# Simple algorithm for estimating brightness (0 to 255)
	weightedBrightness = background.red * 0.3 + background.green * 0.6 + background.blue * 0.1
	
	# (0 to 150) foreground = white, (151 to 255) foreground = black]
	if weightedBrightness > 150:
		return False # If the background is a bright color
	else:
		return True # If the background is a dark color
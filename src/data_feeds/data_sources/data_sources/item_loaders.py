from datetime import datetime

import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from scrapy.loader import ItemLoader

# IMPORT ITEMS HERE
from src.data_feeds.data_sources.data_sources.items import (
    FivethirtyeightPlayerItem,
    InpredictableWPAItem,
    Nba2kPlayerItem,
    NbaStatsBoxscoresAdvAdvancedItem,
    NbaStatsBoxscoresAdvMiscItem,
    NbaStatsBoxscoresAdvScoringItem,
    NbaStatsBoxscoresAdvTraditionalItem,
    NbaStatsBoxscoresAdvUsageItem,
    NbaStatsBoxscoresTraditionalItem,
    NbaStatsGameResultsItem,
    NbaStatsPlayerGeneralAdvancedItem,
    NbaStatsPlayerGeneralDefenseItem,
    NbaStatsPlayerGeneralMiscItem,
    NbaStatsPlayerGeneralOpponentItem,
    NbaStatsPlayerGeneralScoringItem,
    NbaStatsPlayerGeneralTraditionalItem,
    NbaStatsPlayerGeneralUsageItem,
)

# ADD NEW ITEM LOADERS HERE


class NbaStatsGameResultsItemLoader(ItemLoader):
    default_item_class = NbaStatsGameResultsItem
    default_output_processor = TakeFirst()

    game_id_in = MapCompose(str.strip)
    game_date_in = MapCompose(str.strip)
    home_team_id_in = MapCompose(int)
    away_team_id_in = MapCompose(int)
    home_team_in = MapCompose(str.strip)
    away_team_in = MapCompose(str.strip)
    home_score_in = MapCompose(int)
    away_score_in = MapCompose(int)


class NbaStatsPlayerGeneralTraditionalItemLoader(ItemLoader):
    default_item_class = NbaStatsPlayerGeneralTraditionalItem
    default_output_processor = TakeFirst()

    to_date_in = MapCompose(str.strip)
    season_year_in = MapCompose(str)
    season_type_in = MapCompose(str)
    player_id_in = MapCompose(int)
    player_name_in = MapCompose(str)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str)
    age_in = MapCompose(int)
    gp_in = MapCompose(int)
    w_in = MapCompose(int)
    l_in = MapCompose(int)
    w_pct_in = MapCompose(float)
    min_in = MapCompose(float)
    fgm_in = MapCompose(float)
    fga_in = MapCompose(float)
    fg_pct_in = MapCompose(float)
    fg3m_in = MapCompose(float)
    fg3a_in = MapCompose(float)
    fg3_pct_in = MapCompose(float)
    ftm_in = MapCompose(float)
    fta_in = MapCompose(float)
    ft_pct_in = MapCompose(float)
    oreb_in = MapCompose(float)
    dreb_in = MapCompose(float)
    reb_in = MapCompose(float)
    ast_in = MapCompose(float)
    tov_in = MapCompose(float)
    stl_in = MapCompose(float)
    blk_in = MapCompose(float)
    blka_in = MapCompose(float)
    pf_in = MapCompose(float)
    pfd_in = MapCompose(float)
    pts_in = MapCompose(int)
    plus_minus_in = MapCompose(float)
    nba_fantasy_pts_in = MapCompose(float)
    dd2_in = MapCompose(int)
    td3_in = MapCompose(int)


class NbaStatsPlayerGeneralAdvancedItemLoader(ItemLoader):
    default_item_class = NbaStatsPlayerGeneralAdvancedItem
    default_output_processor = TakeFirst()

    to_date_in = MapCompose(str.strip)
    season_year_in = MapCompose(str)
    season_type_in = MapCompose(str)
    player_id_in = MapCompose(int)
    player_name_in = MapCompose(str)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str)
    age_in = MapCompose(int)
    gp_in = MapCompose(int)
    w_in = MapCompose(int)
    l_in = MapCompose(int)
    w_pct_in = MapCompose(float)
    min_in = MapCompose(float)
    e_off_rating_in = MapCompose(float)
    off_rating_in = MapCompose(float)
    sp_work_off_rating_in = MapCompose(float)
    e_def_rating_in = MapCompose(float)
    def_rating_in = MapCompose(float)
    sp_work_def_rating_in = MapCompose(float)
    e_net_rating_in = MapCompose(float)
    net_rating_in = MapCompose(float)
    sp_work_net_rating_in = MapCompose(float)
    ast_pct_in = MapCompose(float)
    ast_to_in = MapCompose(float)
    ast_ratio_in = MapCompose(float)
    oreb_pct_in = MapCompose(float)
    dreb_pct_in = MapCompose(float)
    reb_pct_in = MapCompose(float)
    tm_tov_pct_in = MapCompose(float)
    e_tov_pct_in = MapCompose(float)
    efg_pct_in = MapCompose(float)
    ts_pct_in = MapCompose(float)
    usg_pct_in = MapCompose(float)
    e_usg_pct_in = MapCompose(float)
    e_pace_in = MapCompose(float)
    pace_in = MapCompose(float)
    pace_per40_in = MapCompose(float)
    sp_work_pace_in = MapCompose(float)
    pie_in = MapCompose(float)
    poss_in = MapCompose(int)
    fgm_in = MapCompose(int)
    fga_in = MapCompose(int)
    fgm_pg_in = MapCompose(float)
    fga_pg_in = MapCompose(float)
    fg_pct_in = MapCompose(float)


class NbaStatsPlayerGeneralMiscItemLoader(ItemLoader):
    default_item_class = NbaStatsPlayerGeneralMiscItem
    default_output_processor = TakeFirst()

    to_date_in = MapCompose(str.strip)
    season_year_in = MapCompose(str)
    season_type_in = MapCompose(str)
    player_id_in = MapCompose(int)
    player_name_in = MapCompose(str.strip)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str.strip)
    age_in = MapCompose(int)
    gp_in = MapCompose(int)
    w_in = MapCompose(int)
    l_in = MapCompose(int)
    w_pct_in = MapCompose(float)
    min_in = MapCompose(float)
    pts_off_tov_in = MapCompose(float)
    pts_2nd_chance_in = MapCompose(float)
    pts_fb_in = MapCompose(float)
    pts_paint_in = MapCompose(float)
    opp_pts_off_tov_in = MapCompose(float)
    opp_pts_2nd_chance_in = MapCompose(float)
    opp_pts_fb_in = MapCompose(float)
    opp_pts_paint_in = MapCompose(float)
    blk_in = MapCompose(float)
    blka_in = MapCompose(float)
    pf_in = MapCompose(float)
    pfd_in = MapCompose(float)
    nba_fantasy_pts_in = MapCompose(float)


class NbaStatsPlayerGeneralScoringItemLoader(ItemLoader):
    default_item_class = NbaStatsPlayerGeneralScoringItem
    default_output_processor = TakeFirst()

    to_date_in = MapCompose(str.strip)
    season_year_in = MapCompose(str)
    season_type_in = MapCompose(str)
    player_id_in = MapCompose(int)
    player_name_in = MapCompose(str.strip)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str.strip)
    age_in = MapCompose(int)
    gp_in = MapCompose(int)
    w_in = MapCompose(int)
    l_in = MapCompose(int)
    w_pct_in = MapCompose(float)
    min_in = MapCompose(float)
    pct_fga_2pt_in = MapCompose(float)
    pct_fga_3pt_in = MapCompose(float)
    pct_pts_2pt_in = MapCompose(float)
    pct_pts_2pt_mr_in = MapCompose(float)
    pct_pts_3pt_in = MapCompose(float)
    pct_pts_fb_in = MapCompose(float)
    pct_pts_ft_in = MapCompose(float)
    pct_pts_off_tov_in = MapCompose(float)
    pct_pts_paint_in = MapCompose(float)
    pct_ast_2pm_in = MapCompose(float)
    pct_uast_2pm_in = MapCompose(float)
    pct_ast_3pm_in = MapCompose(float)
    pct_uast_3pm_in = MapCompose(float)
    pct_ast_fgm_in = MapCompose(float)
    pct_uast_fgm_in = MapCompose(float)
    fgm_in = MapCompose(int)
    fga_in = MapCompose(int)
    fg_pct_in = MapCompose(float)


class NbaStatsPlayerGeneralUsageItemLoader(ItemLoader):
    default_item_class = NbaStatsPlayerGeneralUsageItem
    default_output_processor = TakeFirst()

    to_date_in = MapCompose(str.strip)
    season_year_in = MapCompose(str)
    season_type_in = MapCompose(str)
    player_id_in = MapCompose(int)
    player_name_in = MapCompose(str.strip)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str.strip)
    age_in = MapCompose(int)
    gp_in = MapCompose(int)
    w_in = MapCompose(int)
    l_in = MapCompose(int)
    w_pct_in = MapCompose(float)
    min_in = MapCompose(float)
    usg_pct_in = MapCompose(float)
    pct_fgm_in = MapCompose(float)
    pct_fga_in = MapCompose(float)
    pct_fg3m_in = MapCompose(float)
    pct_fg3a_in = MapCompose(float)
    pct_ftm_in = MapCompose(float)
    pct_fta_in = MapCompose(float)
    pct_oreb_in = MapCompose(float)
    pct_dreb_in = MapCompose(float)
    pct_reb_in = MapCompose(float)
    pct_ast_in = MapCompose(float)
    pct_tov_in = MapCompose(float)
    pct_stl_in = MapCompose(float)
    pct_blk_in = MapCompose(float)
    pct_blka_in = MapCompose(float)
    pct_pf_in = MapCompose(float)
    pct_pfd_in = MapCompose(float)
    pct_pts_in = MapCompose(float)


class NbaStatsPlayerGeneralOpponentItemLoader(ItemLoader):
    default_item_class = NbaStatsPlayerGeneralOpponentItem
    default_output_processor = TakeFirst()

    to_date_in = MapCompose(str.strip)
    season_year_in = MapCompose(str)
    season_type_in = MapCompose(str)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str.strip)
    team_name_in = MapCompose(str.strip)
    vs_player_id_in = MapCompose(int)
    vs_player_name_in = MapCompose(str.strip)
    court_status_in = MapCompose(str.strip)
    gp_in = MapCompose(int)
    w_in = MapCompose(int)
    l_in = MapCompose(int)
    w_pct_in = MapCompose(float)
    min_in = MapCompose(float)
    opp_fgm_in = MapCompose(float)
    opp_fga_in = MapCompose(float)
    opp_fg_pct_in = MapCompose(float)
    opp_fg3m_in = MapCompose(float)
    opp_fg3a_in = MapCompose(float)
    opp_fg3_pct_in = MapCompose(float)
    opp_ftm_in = MapCompose(float)
    opp_fta_in = MapCompose(float)
    opp_ft_pct_in = MapCompose(float)
    opp_oreb_in = MapCompose(float)
    opp_dreb_in = MapCompose(float)
    opp_reb_in = MapCompose(float)
    opp_ast_in = MapCompose(float)
    opp_tov_in = MapCompose(float)
    opp_stl_in = MapCompose(float)
    opp_blk_in = MapCompose(float)
    opp_blka_in = MapCompose(float)
    opp_pf_in = MapCompose(float)
    opp_pfd_in = MapCompose(float)
    opp_pts_in = MapCompose(float)
    plus_minus_in = MapCompose(float)


class NbaStatsPlayerGeneralDefenseItemLoader(ItemLoader):
    default_item_class = NbaStatsPlayerGeneralDefenseItem
    default_output_processor = TakeFirst()

    to_date_in = MapCompose(str.strip)
    season_year_in = MapCompose(str)
    season_type_in = MapCompose(str)
    player_id_in = MapCompose(int)
    player_name_in = MapCompose(str.strip)
    nickname_in = MapCompose(str.strip)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str.strip)
    age_in = MapCompose(int)
    gp_in = MapCompose(int)
    w_in = MapCompose(int)
    l_in = MapCompose(int)
    w_pct_in = MapCompose(float)
    min_in = MapCompose(float)
    def_rating_in = MapCompose(float)
    dreb_in = MapCompose(float)
    dreb_pct_in = MapCompose(float)
    pct_dreb_in = MapCompose(float)
    stl_in = MapCompose(float)
    pct_stl_in = MapCompose(float)
    blk_in = MapCompose(float)
    pct_blk_in = MapCompose(float)
    opp_pts_off_tov_in = MapCompose(float)
    opp_pts_2nd_chance_in = MapCompose(float)
    opp_pts_fb_in = MapCompose(float)
    opp_pts_paint_in = MapCompose(float)
    def_ws_in = MapCompose(float)


class NbaStatsBoxscoresTraditionalItemLoader(ItemLoader):
    default_item_class = NbaStatsBoxscoresTraditionalItem
    default_output_processor = TakeFirst()

    season_in = MapCompose(str.strip)
    season_type_in = MapCompose(str.strip)
    player_id_in = MapCompose(int)
    player_in = MapCompose(str.strip)
    team_id_in = MapCompose(int)
    team_in = MapCompose(str.strip)
    game_id_in = MapCompose(str.strip)
    match_up_in = MapCompose(str.strip)
    game_date_in = MapCompose(str.strip)
    w_l_in = MapCompose(str.strip)
    min_in = MapCompose(int)
    pts_in = MapCompose(int)
    fgm_in = MapCompose(int)
    fga_in = MapCompose(int)
    fg_pct_in = MapCompose(float)
    three_pm_in = MapCompose(int)
    three_pa_in = MapCompose(int)
    three_p_pct_in = MapCompose(float)
    ftm_in = MapCompose(int)
    fta_in = MapCompose(int)
    ft_pct_in = MapCompose(float)
    oreb_in = MapCompose(int)
    dreb_in = MapCompose(int)
    reb_in = MapCompose(int)
    ast_in = MapCompose(int)
    stl_in = MapCompose(int)
    blk_in = MapCompose(int)
    tov_in = MapCompose(int)
    pf_in = MapCompose(int)
    plus_minus_in = MapCompose(int)
    fp_in = MapCompose(float)


class NbaStatsBoxscoresAdvTraditionalItemLoader(ItemLoader):
    default_item_class = NbaStatsBoxscoresAdvTraditionalItem
    default_output_processor = TakeFirst()

    season_year_in = MapCompose(str.strip)
    season_type_in = MapCompose(str.strip)
    player_id_in = MapCompose(int)
    player_name_in = MapCompose(str.strip)
    nickname_in = MapCompose(str.strip)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str.strip)
    team_name_in = MapCompose(str.strip)
    game_id_in = MapCompose(str.strip)
    game_date_in = MapCompose(str.strip)
    matchup_in = MapCompose(str.strip)
    w_l_in = MapCompose(str.strip)
    min_in = MapCompose(float)
    fgm_in = MapCompose(float)
    fga_in = MapCompose(float)
    fg_pct_in = MapCompose(float)
    three_pm_in = MapCompose(float)
    three_pa_in = MapCompose(float)
    three_p_pct_in = MapCompose(float)
    ftm_in = MapCompose(float)
    fta_in = MapCompose(float)
    ft_pct_in = MapCompose(float)
    oreb_in = MapCompose(float)
    dreb_in = MapCompose(float)
    reb_in = MapCompose(float)
    ast_in = MapCompose(float)
    tov_in = MapCompose(float)
    stl_in = MapCompose(float)
    blk_in = MapCompose(float)
    blka_in = MapCompose(float)
    pf_in = MapCompose(float)
    pfd_in = MapCompose(float)
    pts_in = MapCompose(float)
    plus_minus_in = MapCompose(float)
    nba_fantasy_pts_in = MapCompose(float)
    dd2_in = MapCompose(float)
    td3_in = MapCompose(float)


class NbaStatsBoxscoresAdvAdvancedItemLoader(ItemLoader):
    default_item_class = NbaStatsBoxscoresAdvAdvancedItem
    default_output_processor = TakeFirst()

    season_type_in = MapCompose(str.strip)
    season_year_in = MapCompose(str.strip)
    player_id_in = MapCompose(int)
    player_name_in = MapCompose(str.strip)
    nickname_in = MapCompose(str.strip)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str.strip)
    team_name_in = MapCompose(str.strip)
    game_id_in = MapCompose(str.strip)
    game_date_in = MapCompose(str.strip)
    matchup_in = MapCompose(str.strip)
    w_l_in = MapCompose(str.strip)
    min_in = MapCompose(float)
    e_off_rating_in = MapCompose(float)
    off_rating_in = MapCompose(float)
    sp_work_off_rating_in = MapCompose(float)
    e_def_rating_in = MapCompose(float)
    def_rating_in = MapCompose(float)
    sp_work_def_rating_in = MapCompose(float)
    e_net_rating_in = MapCompose(float)
    net_rating_in = MapCompose(float)
    sp_work_net_rating_in = MapCompose(float)
    ast_pct_in = MapCompose(float)
    ast_to_in = MapCompose(float)
    ast_ratio_in = MapCompose(float)
    oreb_pct_in = MapCompose(float)
    dreb_pct_in = MapCompose(float)
    reb_pct_in = MapCompose(float)
    tm_tov_pct_in = MapCompose(float)
    e_tov_pct_in = MapCompose(float)
    efg_pct_in = MapCompose(float)
    ts_pct_in = MapCompose(float)
    usg_pct_in = MapCompose(float)
    e_usg_pct_in = MapCompose(float)
    e_pace_in = MapCompose(float)
    pace_in = MapCompose(float)
    pace_per40_in = MapCompose(float)
    sp_work_pace_in = MapCompose(float)
    pie_in = MapCompose(float)
    poss_in = MapCompose(int)
    fgm_in = MapCompose(int)
    fga_in = MapCompose(int)
    fgm_pg_in = MapCompose(float)
    fga_pg_in = MapCompose(float)
    fg_pct_in = MapCompose(float)


class NbaStatsBoxscoresAdvMiscItemLoader(ItemLoader):
    default_item_class = NbaStatsBoxscoresAdvMiscItem
    default_output_processor = TakeFirst()

    season_type_in = MapCompose(str.strip)
    season_year_in = MapCompose(str.strip)
    player_id_in = MapCompose(int)
    player_name_in = MapCompose(str.strip)
    nickname_in = MapCompose(str.strip)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str.strip)
    team_name_in = MapCompose(str.strip)
    game_id_in = MapCompose(str.strip)
    game_date_in = MapCompose(str.strip)
    matchup_in = MapCompose(str.strip)
    w_l_in = MapCompose(str.strip)
    min_in = MapCompose(float)
    pts_off_tov_in = MapCompose(int)
    pts_2nd_chance_in = MapCompose(int)
    pts_fb_in = MapCompose(int)
    pts_paint_in = MapCompose(int)
    opp_pts_off_tov_in = MapCompose(int)
    opp_pts_2nd_chance_in = MapCompose(int)
    opp_pts_fb_in = MapCompose(int)
    opp_pts_paint_in = MapCompose(int)
    blk_in = MapCompose(int)
    blka_in = MapCompose(int)
    pf_in = MapCompose(int)
    pfd_in = MapCompose(int)
    nba_fantasy_pts_in = MapCompose(float)


class NbaStatsBoxscoresAdvScoringItemLoader(ItemLoader):
    default_item_class = NbaStatsBoxscoresAdvScoringItem
    default_output_processor = TakeFirst()

    season_type_in = MapCompose(str.strip)
    season_year_in = MapCompose(str.strip)
    player_id_in = MapCompose(int)
    player_name_in = MapCompose(str.strip)
    nickname_in = MapCompose(str.strip)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str.strip)
    team_name_in = MapCompose(str.strip)
    game_id_in = MapCompose(str.strip)
    game_date_in = MapCompose(str.strip)
    matchup_in = MapCompose(str.strip)
    w_l_in = MapCompose(str.strip)
    min_in = MapCompose(float)
    pct_fga_2pt_in = MapCompose(float)
    pct_fga_3pt_in = MapCompose(float)
    pct_pts_2pt_in = MapCompose(float)
    pct_pts_2pt_mr_in = MapCompose(float)
    pct_pts_3pt_in = MapCompose(float)
    pct_pts_fb_in = MapCompose(float)
    pct_pts_ft_in = MapCompose(float)
    pct_pts_off_tov_in = MapCompose(float)
    pct_pts_paint_in = MapCompose(float)
    pct_ast_2pm_in = MapCompose(float)
    pct_uast_2pm_in = MapCompose(float)
    pct_ast_3pm_in = MapCompose(float)
    pct_uast_3pm_in = MapCompose(float)
    pct_ast_fgm_in = MapCompose(float)
    pct_uast_fgm_in = MapCompose(float)
    fgm_in = MapCompose(float)
    fga_in = MapCompose(float)
    fg_pct_in = MapCompose(float)


class NbaStatsBoxscoresAdvUsageItemLoader(ItemLoader):
    default_item_class = NbaStatsBoxscoresAdvUsageItem
    default_output_processor = TakeFirst()

    season_type_in = MapCompose(str.strip)
    season_year_in = MapCompose(str.strip)
    player_id_in = MapCompose(int)
    player_name_in = MapCompose(str.strip)
    nickname_in = MapCompose(str.strip)
    team_id_in = MapCompose(int)
    team_abbreviation_in = MapCompose(str.strip)
    team_name_in = MapCompose(str.strip)
    game_id_in = MapCompose(str.strip)
    game_date_in = MapCompose(str.strip)
    matchup_in = MapCompose(str.strip)
    w_l_in = MapCompose(str.strip)
    min_in = MapCompose(int)
    usg_pct_in = MapCompose(float)
    pct_fgm_in = MapCompose(float)
    pct_fga_in = MapCompose(float)
    pct_fg3m_in = MapCompose(float)
    pct_fg3a_in = MapCompose(float)
    pct_ftm_in = MapCompose(float)
    pct_fta_in = MapCompose(float)
    pct_oreb_in = MapCompose(float)
    pct_dreb_in = MapCompose(float)
    pct_reb_in = MapCompose(float)
    pct_ast_in = MapCompose(float)
    pct_tov_in = MapCompose(float)
    pct_stl_in = MapCompose(float)
    pct_blk_in = MapCompose(float)
    pct_blka_in = MapCompose(float)
    pct_pf_in = MapCompose(float)
    pct_pfd_in = MapCompose(float)
    pct_pts_in = MapCompose(float)


class Nba2kPlayerItemLoader(ItemLoader):
    default_item_class = Nba2kPlayerItem
    default_output_processor = TakeFirst()

    access_date_in = MapCompose(str.strip)
    player_name_in = MapCompose(str.strip)
    bronze_badges_in = MapCompose(int)
    silver_badges_in = MapCompose(int)
    gold_badges_in = MapCompose(int)
    hall_of_fame_badges_in = MapCompose(int)
    outside_scoring_in = MapCompose(int)
    close_shot_in = MapCompose(int)
    mid_range_shot_in = MapCompose(int)
    three_point_shot_in = MapCompose(int)
    free_throw_in = MapCompose(int)
    shot_iq_in = MapCompose(int)
    offensive_consistency_in = MapCompose(int)
    athleticism_in = MapCompose(int)
    speed_in = MapCompose(int)
    acceleration_in = MapCompose(int)
    strength_in = MapCompose(int)
    vertical_in = MapCompose(int)
    stamina_in = MapCompose(int)
    hustle_in = MapCompose(int)
    overall_durability_in = MapCompose(int)
    inside_scoring_in = MapCompose(int)
    layup_in = MapCompose(int)
    standing_dunk_in = MapCompose(int)
    driving_dunk_in = MapCompose(int)
    post_hook_in = MapCompose(int)
    post_fade_in = MapCompose(int)
    post_control_in = MapCompose(int)
    draw_foul_in = MapCompose(int)
    hands_in = MapCompose(int)
    playmaking_in = MapCompose(int)
    pass_accuracy_in = MapCompose(int)
    ball_handle_in = MapCompose(int)
    speed_with_ball_in = MapCompose(int)
    pass_iq_in = MapCompose(int)
    pass_vision_in = MapCompose(int)
    defending_in = MapCompose(int)
    interior_defense_in = MapCompose(int)
    perimeter_defense_in = MapCompose(int)
    steal_in = MapCompose(int)
    block_in = MapCompose(int)
    lateral_quickness_in = MapCompose(int)
    help_defense_iq_in = MapCompose(int)
    pass_perception_in = MapCompose(int)
    defensive_consistency_in = MapCompose(int)
    rebounding_in = MapCompose(int)
    offensive_rebound_in = MapCompose(int)
    defensive_rebound_in = MapCompose(int)
    intangibles_in = MapCompose(int)
    potential_in = MapCompose(int)
    total_attributes_in = MapCompose(int)


class FivethirtyeightPlayerItemLoader(ItemLoader):
    default_item_class = FivethirtyeightPlayerItem
    default_output_processor = TakeFirst()

    priority_in = MapCompose(int)
    to_date_in = MapCompose()
    player_name_in = MapCompose(str.strip)
    player_id_in = MapCompose(str.strip)
    season_in = MapCompose(int)
    poss_in = MapCompose(int)
    mp_in = MapCompose(int)
    raptor_box_offense_in = MapCompose(float)
    raptor_box_defense_in = MapCompose(float)
    raptor_box_total_in = MapCompose(float)
    raptor_onoff_offense_in = MapCompose(float)
    raptor_onoff_defense_in = MapCompose(float)
    raptor_onoff_total_in = MapCompose(float)
    raptor_offense_in = MapCompose(float)
    raptor_defense_in = MapCompose(float)
    raptor_total_in = MapCompose(float)
    war_total_in = MapCompose(float)
    war_reg_season_in = MapCompose(float)
    war_playoffs_in = MapCompose(float)
    predator_offense_in = MapCompose(float)
    predator_defense_in = MapCompose(float)
    predator_total_in = MapCompose(float)
    pace_impact_in = MapCompose(float)


class InpredictableWPAItemLoader(ItemLoader):
    default_item_class = InpredictableWPAItem
    default_output_processor = TakeFirst()

    rnk_in = MapCompose(int)
    player_in = MapCompose(str.strip)
    pos_in = MapCompose(str.strip)
    gms_in = MapCompose(int)
    wpa_in = MapCompose(float)
    ewpa_in = MapCompose(float)
    clwpa_in = MapCompose(float)
    gbwpa_in = MapCompose(float)
    sh_in = MapCompose(float)
    to_in = MapCompose(float)
    ft_in = MapCompose(float)
    reb_in = MapCompose(float)
    ast_in = MapCompose(float)
    stl_in = MapCompose(float)
    blk_in = MapCompose(float)
    kwpa_in = MapCompose(float)
    to_date_in = MapCompose(str.strip)